# Nombre del Proyecto

[![Django](https://img.shields.io/badge/Django-4.2-brightgreen)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.14-blue)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/Docker-✔-blue)](https://www.docker.com/)

## 📝 API de lista de tareas (TODO)
API RESTful creada con Python y Django para el manejo de un lista de tareas 

## 🛠️ Configuración del Entorno Local

### Requisitos previos
- Docker Engine 20.10+
- Docker Compose 1.29+
- Python 3.9+ (opcional para desarrollo sin Docker)

### Instrucciones para correr proyecto

#### Clonar el repositorio:
```bash
    git clone https://github.com/tu-usuario/tu-proyecto.git
    cd tu-proyecto
```
#### Construir imágenes y levantar contenedores
    
    docker-compose up --build web
   
### Corres test:
    
    docker-compose run --rm web python manage.py test
    
#### Permisos solo en Linux o subsistema WSL
    chmod -R 755 . && find . -type f -exec chmo 644 {} \;

### Comandos utiles:

#### Detener contenedores
    docker-compose down

#### Formatear el codigo
    docker-compose run --rm format

#### Correr migraiones
    docker-compose run --rm web python manage.py makemigrations

    docker-compose run --rm web python manage.py migrate
