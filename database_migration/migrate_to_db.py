import pandas as pd
import pyodbc
from azure.storage.blob import BlobServiceClient
from io import BytesIO
from dotenv import load_dotenv
import os


load_dotenv()  # Carga las variables de entorno desde '.env'.

# Configuración Azure Blob Storage
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "archivos"

# Configuración de la conexión a Azure SQL Database
server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USERNAME')
password = os.getenv('SQL_PASSWORD')

# utilizando el driver ODBC 18 para SQL Server
cnxn_str = f"Driver={{ODBC Driver 18 for SQL Server}};Server={server},1433;Database=employeedirectorydb;UID={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=220;"

# Crear una instancia del servicio BlobServiceClient y obtener un cliente para el contenedor específico
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Establecer conexión con Azure SQL Database
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

def verificar_o_crear_tabla(df, table_name):
    # Determinar el tipo de columna SQL adecuado para cada columna del DataFrame
    column_types = []
    for col_name, dtype in zip(df.columns, df.dtypes):
        sql_type = "VARCHAR(MAX)"
        if "int" in str(dtype): sql_type = "INT"
        elif "float" in str(dtype): sql_type = "FLOAT"
        elif "datetime" in str(dtype): sql_type = "DATETIME"
        column_types.append(f"{col_name} {sql_type}")
    columns_sql = ", ".join(column_types)
    
    create_table_sql = f"IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '{table_name}') BEGIN CREATE TABLE {table_name} ({columns_sql}); END;"
    cursor.execute(create_table_sql)
    cursor.commit()

# Función para cargar datos desde un archivo Parquet en Azure Blob Storage a Azure SQL Database
def cargar_datos_parquet_a_sql(archivo_parquet):
    # Obtener los datos del blob y cargarlos en un DataFrame de Pandas
    blob_client = container_client.get_blob_client(blob=archivo_parquet)
    blob_data = blob_client.download_blob().readall()
    df = pd.read_parquet(BytesIO(blob_data))
    
    # Determinar el nombre de la tabla a partir del nombre del archivo Parquet
    table_name = archivo_parquet.replace(".parquet", "")
    
    # Verificar si la tabla existe y crearla si no
    verificar_o_crear_tabla(df, table_name)

    # Insertar los datos del DataFrame en la tabla SQL
    for index, row in df.iterrows():
        placeholders = ', '.join(['?' for _ in row])  # Crear placeholders para la consulta SQL
        columns = ', '.join(row.keys())
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row.values))
    
    cnxn.commit()

# Listar todos los blobs en el contenedor y cargar los archivos Parquet a la base de datos SQL
blob_list = container_client.list_blobs()
for blob in blob_list:
    if blob.name.endswith('.parquet'):
        cargar_datos_parquet_a_sql(blob.name)

cnxn.close()