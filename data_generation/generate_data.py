import pandas as pd
import numpy as np
from datetime import datetime

# Configurar la semilla para reproducibilidad
# Esto garantiza que los resultados sean los mismos cada vez que se ejecute el script,
# lo cual es útil para pruebas y depuración.
np.random.seed(0)

# Crear un diccionario con dos listas: una para ID de departamento y otra para nombres de departamento.
departamentos_data = {
    "departamento_id": np.arange(1, 11),  # Generar IDs de departamento del 1 al 10
    "nombre_departamento": ["Marketing", "Ventas", "TI", "RRHH", "Finanzas", "Operaciones", "Legal", "Compras", "Diseño", "Educación"]
}

puestos_data = {
    "puesto_id": np.arange(1, 21), 
    "nombre_puesto": [f"Puesto {i}" for i in np.arange(1, 21)],  # Crear nombres de puestos con formato "Puesto i"
    "departamento_id": np.random.choice(departamentos_data["departamento_id"], 20)  # Asignar aleatoriamente IDs de departamento a cada puesto
}

# Crear un diccionario con los datos de los empleados, incluyendo IDs, nombres, IDs de puesto, fechas de contratación y salarios.
empleados_data = {
    "empleado_id": np.arange(1, 101),  # Generar IDs de empleado del 1 al 100
    "nombre_empleado": [f"Empleado {i}" for i in np.arange(1, 101)],  # Crear nombres de empleados con formato "Empleado i"
    "puesto_id": np.random.choice(puestos_data["puesto_id"], 100),  # Asignar aleatoriamente IDs de puestos a cada empleado
    "fecha_contratacion": [datetime(2021, np.random.randint(1, 13), np.random.randint(1, 29)) for _ in range(100)],  # Generar fechas de contratación aleatorias dentro del año 2021
    "salario": np.random.uniform(30000, 80000, 100).round(2)  # Generar salarios aleatorios entre 30,000 y 80,000, redondeados a dos decimales
}

departamentos_df = pd.DataFrame(departamentos_data)
puestos_df = pd.DataFrame(puestos_data)
empleados_df = pd.DataFrame(empleados_data)

print(departamentos_df.head())
print(puestos_df.head())
print(empleados_df.head())
