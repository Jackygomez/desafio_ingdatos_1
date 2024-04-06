FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor a /app. 
WORKDIR /app

# Actualizar la lista de paquetes e instalar unixodbc y unixodbc-dev.
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev

COPY requirements.txt .

# Instalar las dependencias del archivo requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

COPY API_REST ./API_REST

EXPOSE 5000
 
CMD ["python", "API_REST/app.py"]
