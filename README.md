# TecnoEmpleados

TecnoEmpleados es una aplicación web desarrollada con Django para la administración de empleados. La aplicación permite realizar operaciones de creación, lectura, actualización y eliminación (CRUD) de empleados, así como autenticación de usuarios (registro, inicio y cierre de sesión) y filtrado/ordenamiento de la información.

## Características

- **Autenticación de Usuarios:** 
  - Registro, inicio de sesión y cierre de sesión.
  - Puedes registrarte en la aplicación o utilizar las credenciales proporcionadas (ver sección de credenciales).

- **Gestión de Empleados:** 
  - Crear, editar, listar y eliminar empleados.
  - Validaciones en el formulario para que la cédula y el teléfono tengan al menos 10 dígitos y la fecha de nacimiento sea obligatoria.
  
- **Búsqueda y Filtrado:** 
  - Búsqueda en un único campo que consulta en nombre, cédula y correo.
  - Ordenamiento por nombre, cédula, email y fecha de nacimiento.

- **Interfaz Moderna:** 
  - Diseño responsivo basado en Bootstrap 5 y Bootstrap Icons.

## Despliegue en Railway

La conexión a la base de datos ya está configurada para el despliegue en Railway, por lo que **no es necesario configurar manualmente la base de datos**. La variable de entorno `DATABASE_URL` se utiliza para conectarse a la base de datos de Railway.

## Credenciales de Acceso

Si aún no tienes cuenta, puedes **registrarte** directamente en la aplicación.  
Si prefieres utilizar las credenciales de ejemplo (reemplaza estos valores por las reales o consulta el canal de comunicación del equipo):

- **Usuario:** demo_user
- **Contraseña:** demo_password

## Instalación y Uso

### Requisitos

- Python 3.8+
- Django 3.2+ (o superior)
- PostgreSQL (en desarrollo local, si decides probarlo en local)
- [dj-database-url](https://pypi.org/project/dj-database-url/)
- Docker (opcional)

### Instalación Local

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/jpbuelvas/django-tecno
   cd django-tecno
2. **Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    # En Linux/Mac:
    source venv/bin/activate
    # En Windows:
    venv\Scripts\activate

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt

4. **Aplica las migraciones:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Crea un superusuario (opcional):**

    ```bash
    python manage.py createsuperuser

6. **Inicia el servidor de desarrollo:**

    ```bash
    python manage.py runserver

## Uso con Docker de Acceso

Si prefieres usar Docker para ejecutar la aplicación, asegúrate de tener Docker instalado y ejecuta los siguientes comandos:

1. **Construir la imagen:**

    ```bash
    docker build -t nombre_de_tu_imagen .

2. **Ejecutar el contenedor:**
    ```bash
    docker run -d -p 8000:8000 nombre_de_tu_imagen

La aplicación estará disponible en http://localhost:8000.

## Estructura del Proyecto

- **employees/: Contiene el modelo de empleados, vistas, formularios y templates específicos para la gestión de empleados.** 
- **templates/: Plantillas HTML basadas en Bootstrap para todas las vistas (home, login, registro, listado, creación y edición de empleados).** 
- **Dockerfile: Archivo de configuración para construir la imagen Docker.** 
- **requirements.txt: Lista de dependencias del proyecto.** 
- **README.md: Este archivo.** 

