# Usa una imagen oficial de Python como base
FROM python:3.13

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
# Copia el resto del código de la aplicación
COPY . /app/

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
