from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()  # Carga las variables de entorno desde '.env'.

class Config:
    DATABASE_SERVER = os.getenv('SQL_SERVER')
    DATABASE_NAME = os.getenv('SQL_DATABASE')
    DATABASE_USERNAME = os.getenv('SQL_USERNAME')
    DATABASE_PASSWORD = os.getenv('SQL_PASSWORD')
    DATABASE_CONNECTION_STRING = f'Driver={{ODBC Driver 18 for SQL Server}};Server={DATABASE_SERVER},1433;Database={DATABASE_NAME};UID={DATABASE_USERNAME};Pwd={DATABASE_PASSWORD};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=220;'
