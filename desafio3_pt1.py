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

cnxn_str = f"Driver={{ODBC Driver 18 for SQL Server}};Server={server},1433;Database=employeedirectorydb;UID={username};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=220;"

# Conexión a Azure Blob Storage
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Iniciar conexión a SQL
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()

# Función para verificar y crear la tabla si no existe
def verificar_o_crear_tabla(df, table_name):
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

# Función para cargar datos desde Parquet a SQL
def cargar_datos_parquet_a_sql(archivo_parquet):
    blob_client = container_client.get_blob_client(blob=archivo_parquet)
    blob_data = blob_client.download_blob().readall()
    df = pd.read_parquet(BytesIO(blob_data))
    
    table_name = archivo_parquet.replace(".parquet", "")
    
    verificar_o_crear_tabla(df, table_name)

    # Preparar y ejecutar el INSERT SQL (simplificado para este ejemplo)
    for index, row in df.iterrows():
        placeholders = ', '.join(['?' for _ in row])
        columns = ', '.join(row.keys())
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(row.values))
    
    cnxn.commit()

blob_list = container_client.list_blobs()
for blob in blob_list:
    if blob.name.endswith('.parquet'):
        cargar_datos_parquet_a_sql(blob.name)

cnxn.close()
