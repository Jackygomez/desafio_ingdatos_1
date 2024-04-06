from azure.storage.blob import BlobServiceClient
import pandas as pd
from io import BytesIO
from desafio1_pt1 import departamentos_df, puestos_df, empleados_df
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde '.env'.

# Configuración Azure Blob Storage
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = "archivos"

# Instancia del servicio BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Función para guardar y subir un DataFrame en Azure Blob Storage como archivo CSV y Parquet
def guardar_y_subir_df(df, nombre_base_archivo):
    # Para CSV
    buffer_csv = BytesIO()
    df.to_csv(buffer_csv, index=False)
    buffer_csv.seek(0)  # Regresar al inicio del buffer
    blob_client_csv = container_client.get_blob_client(f'{nombre_base_archivo}.csv')
    blob_client_csv.upload_blob(buffer_csv, overwrite=True)

    # Para Parquet
    buffer_parquet = BytesIO()
    df.to_parquet(buffer_parquet, index=False)
    buffer_parquet.seek(0)  # Regresar al inicio del buffer
    blob_client_parquet = container_client.get_blob_client(f'{nombre_base_archivo}.parquet')
    blob_client_parquet.upload_blob(buffer_parquet, overwrite=True)

# Guardar y subir los DataFrames en Azure Blob Storage como CSV y Parquet
guardar_y_subir_df(departamentos_df, 'departamentos')
guardar_y_subir_df(puestos_df, 'puestos')
guardar_y_subir_df(empleados_df, 'empleados')