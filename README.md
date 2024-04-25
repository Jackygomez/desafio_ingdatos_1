Implementación de ETL en la nube. Documentación resumen y despliegue en GitHub.

1. Generación de Datos Automatizada
Herramientas Utilizadas: Python con bibliotecas Pandas y NumPy.
Proceso: El script de Python genera datos simulados para departamentos, puestos de trabajo y empleados.
2. Almacenamiento de Datos en Formatos CSV/Parquet
Herramientas Utilizadas: Python con la biblioteca Pandas.
Proceso: Los datos generados se almacenan en archivos CSV y Parquet, tanto localmente como en Azure Blob Storage.
3. Migración de Datos a una Base de Datos
Herramientas Utilizadas: Azure Blob Storage para almacenamiento de datos, Python con pyodbc para la conexión a bases de datos, y Azure SQL Database como sistema de gestión de bases de datos.
Proceso: Un proceso batch implementado en Python carga los datos desde archivos Parquet en Azure Blob Storage a tablas en Azure SQL Database.
4. Creación de Vista en Azure SQL Database
Herramientas Utilizadas: Azure SQL Database.
Proceso: Se utiliza SQL para crear una vista que facilite el acceso a información relevante combinada de empleados, puestos y departamentos.
5. Desarrollo de una API REST para Consultar la Vista
Herramientas Utilizadas: Flask como framework de Python para el desarrollo de la API.
Proceso: Se desarrolla una API REST que permite consultar la vista VistaDetallesEmpleados en Azure SQL Database y devuelve los datos en formato JSON.
6. Mejora e Implementación de la API con Contenedores
Herramientas Utilizadas: Docker para contenerización.
Proceso: La API desarrollada en Flask se conteneriza utilizando Docker para facilitar el despliegue y la escalabilidad.

NOTA: El detalle de esta prueba se encuentra en https://tasty-pulsar-899.notion.site/Prueba-Tecnica-Ing-datos-6b7c9a0b465c426c9d23b990bb31d380?pvs=4
