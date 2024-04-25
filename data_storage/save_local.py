import os
import pandas as pd
import sys
sys.path.append('D:\desafio_ingdatos_1\data_generation')
from generate_data import departamentos_df, puestos_df, empleados_df
nombre_carpeta = "archivos"

nombre_carpeta = "archivos"

# Verificar si la carpeta existe, si no, crearla
if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)

# Función para guardar DataFrames en CSV y Parquet
def guardar_datos():

    departamentos_df.to_csv(f'{nombre_carpeta}/departamentos.csv', index=False)
    puestos_df.to_csv(f'{nombre_carpeta}/puestos.csv', index=False)
    empleados_df.to_csv(f'{nombre_carpeta}/empleados.csv', index=False)
    
    departamentos_df.to_parquet(f'{nombre_carpeta}/departamentos.parquet', index=False)
    puestos_df.to_parquet(f'{nombre_carpeta}/puestos.parquet', index=False)
    empleados_df.to_parquet(f'{nombre_carpeta}/empleados.parquet', index=False)

guardar_datos()

