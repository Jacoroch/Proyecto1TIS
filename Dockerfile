# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponer el puerto 8080 para Cloud Run
EXPOSE 8080

# Comando para iniciar la aplicación en el puerto 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
