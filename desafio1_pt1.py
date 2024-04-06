import pandas as pd
import numpy as np
from datetime import datetime

# Configurando la semilla para reproducibilidad
np.random.seed(0)

# Datos de Departamentos
departamentos_data = {
    "departamento_id": np.arange(1, 11),
    "nombre_departamento": ["Marketing", "Ventas", "TI", "RRHH", "Finanzas", "Operaciones", "Legal", "Compras", "Diseño", "Educación"]
}

# Datos de Puestos de Trabajo
puestos_data = {
    "puesto_id": np.arange(1, 21),
    "nombre_puesto": [f"Puesto {i}" for i in np.arange(1, 21)],
    "departamento_id": np.random.choice(departamentos_data["departamento_id"], 20)
}

# Datos de Empleados
empleados_data = {
    "empleado_id": np.arange(1, 101),
    "nombre_empleado": [f"Empleado {i}" for i in np.arange(1, 101)],
    "puesto_id": np.random.choice(puestos_data["puesto_id"], 100),
    "fecha_contratacion": [datetime(2021, np.random.randint(1, 13), np.random.randint(1, 29)) for _ in range(100)],
    "salario": np.random.uniform(30000, 80000, 100).round(2)
}

# Convertir a DataFrames de Pandas
departamentos_df = pd.DataFrame(departamentos_data)
puestos_df = pd.DataFrame(puestos_data)
empleados_df = pd.DataFrame(empleados_data)

print(departamentos_df.head())
print(puestos_df.head())
print(empleados_df.head())
