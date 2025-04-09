# Reto Crehana - API de Lista de Tareas

![Django](https://img.shields.io/badge/Django-3.2-green)
![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-blue)
![Docker](https://img.shields.io/badge/Docker-24.0-yellow)
![Python](https://img.shields.io/badge/Python-3.10+-blue)

API RESTful construida con Django REST Framework y Docker para gestión de tareas (operaciones CRUD).

## Características Principales
- Operaciones CRUD para tareas
- Endpoints RESTful
- Base de datos SQLite (desarrollo)
- Dockerizada para fácil despliegue
- Formateo de código con Flake8
- Configuración completa de pruebas
- Poetry para gestión de dependencias

## Estructura del Proyecto ToDoList
    crehana_challenge/
    ├── todolist/ # Configuración principal del proyecto Django
    │ ├── init.py
    │ ├── asgi.py # Configuración ASGI para despliegue
    │ ├── settings.py # Configuración del proyecto
    │ ├── urls.py # URLs principales
    │ └── wsgi.py # Configuración WSGI para despliegue
    │
    ├── todolistapp/ # Aplicación principal
    │ ├── migrations/ # Migraciones de base de datos
    │ ├── init.py
    │ ├── admin.py # Panel de administración
    │ ├── apps.py # Configuración de la app
    │ ├── models.py # Modelos de datos
    │ ├── serializers.py # Serializadores para DRF
    │ ├── tests.py # Pruebas unitarias
    │ ├── urls.py # URLs de la app
    │ ├── utils.py # Utilidades
    │ └── views.py # Controladores
    │
    ├── .flake8 # Configuración de linter
    ├── db.sqlite3 # Base de datos local (dev)
    ├── docker-compose.yml # Configuración multi-contenedor
    ├── Dockerfile # Configuración del contenedor
    ├── manage.py # CLI de Django
    ├── pyproject.toml # Dependencias (Poetry)
    ├── pytest.ini # Configuración de tests
    ├── README.md # Documentación
    └── requirements.txt # Dependencias (pip)

### Estructura Django típica:
1. **Carpeta raíz del proyecto** (`todolist/`):
   - Contiene configuración global (settings, URLs principales)
   - Archivos de despliegue (WSGI/ASGI)

2. **App principal** (`todolistapp/`):
   - Sigue el patrón MVT (Models-Views-Templates)
   - Incluye serializadores para REST API

3. **Herramientas de desarrollo**:
   - Docker para containerización
   - Poetry/pip para gestión de dependencias
   - Pytest para testing
    
## Configuración del Entorno Local

### Requisitos Previos
- Docker Engine 20.10+
- Docker Compose 1.29+

### Instalación
    git clone https://github.com/libardo2s/crehana_challenge.git
    cd crehana_challenge

### Ejecutar el Proyecto
    
    docker-compose up --build web

    La API estará disponible en: http://localhost:8000/api/tasks/
   
### Comandos de Desarrollo:

#### Aplicar Migraciones
    docker-compose run --rm web python manage.py makemigrations
    docker-compose run --rm web python manage.py migrate

#### Ejecutar Pruebas
    docker-compose run --rm test

    Nota: asegurarse de correr las migraciones primero antes de correr los tests

#### Formatear Código
    docker-compose run --rm format

#### Detener Contenedores
    docker-compose down
    
#### Permisos en Linux/WSL (si es necesario)
    chmod -R 755 . && find . -type f -exec chmo 644 {} \;

## Configuración del Entorno Local
    
#### Endpoints

    GET /api/tasks/ - Listar todas las tareas
    POST /api/tasks/ - Crear nueva tarea
    GET /api/tasks/{id}/ - Obtener tarea específica
    PUT /api/tasks/{id}/ - Actualizar tarea
    DELETE /api/tasks/{id}/ - Eliminar tarea (Soft delete)

#### Ejemplo de Request (Crear Tarea)

    POST /api/tasks/
    {
        "title": "Completar reto",
        "description": "Terminar el reto de Crehana",
        "completed": false
    }