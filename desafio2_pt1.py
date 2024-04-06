import os
import pandas as pd
from desafio1_pt1 import departamentos_df, puestos_df, empleados_df

nombre_carpeta = "archivos"

# Verificar si la carpeta existe, si no, crearla
if not os.path.exists(nombre_carpeta):
    os.makedirs(nombre_carpeta)

# Función para guardar DataFrames en CSV y Parquet
def guardar_datos():
    # Guardar en formato CSV
    departamentos_df.to_csv(f'{nombre_carpeta}/departamentos.csv', index=False)
    puestos_df.to_csv(f'{nombre_carpeta}/puestos.csv', index=False)
    empleados_df.to_csv(f'{nombre_carpeta}/empleados.csv', index=False)
    
    # Guardar en formato Parquet
    departamentos_df.to_parquet(f'{nombre_carpeta}/departamentos.parquet', index=False)
    puestos_df.to_parquet(f'{nombre_carpeta}/puestos.parquet', index=False)
    empleados_df.to_parquet(f'{nombre_carpeta}/empleados.parquet', index=False)

guardar_datos()

