from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import BytesIO
from desafio1_pt1 import departamentos_df, puestos_df, empleados_df
from dotenv import load_dotenv
import os

# Carga las variables de entorno desde el archivo '.env'.
load_dotenv()

# Configuración para Azure Blob Storage
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "archivos" 

# Crear una instancia de BlobServiceClient utilizando la cadena de conexión
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Función para guardar y subir un DataFrame a Azure Blob Storage 
def guardar_y_subir_df(df, nombre_base_archivo):
 
    buffer_csv = BytesIO()  # Crear un buffer en memoria para el archivo 
    df.to_csv(buffer_csv, index=False)  # Convertir el DataFrame a CSV y escribirlo en el buffer
    buffer_csv.seek(0)  # Regresar al inicio del buffer para leer desde el principio
    blob_client_csv = container_client.get_blob_client(f'{nombre_base_archivo}.csv')  # Crear un cliente blob para el archivo CSV
    blob_client_csv.upload_blob(buffer_csv, overwrite=True)  # Subir el contenido del buffer como un blob CSV

   
    buffer_parquet = BytesIO()  
    df.to_parquet(buffer_parquet, index=False)  
    buffer_parquet.seek(0)  
    blob_client_parquet = container_client.get_blob_client(f'{nombre_base_archivo}.parquet')  
    blob_client_parquet.upload_blob(buffer_parquet, overwrite=True)  

guardar_y_subir_df(departamentos_df, 'departamentos')
guardar_y_subir_df(puestos_df, 'puestos')
guardar_y_subir_df(empleados_df, 'empleados')
