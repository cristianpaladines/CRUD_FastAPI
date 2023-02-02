# my-movie-app
# Base de datos de películas con FastAPI

Este proyecto es una pequeña aplicación de base de datos de películas construida con el framework de Python FastAPI. La aplicación permite crear, leer, actualizar y eliminar (CRUD) información sobre películas en una base de datos.

# Requisitos

- Python 3.7 o superior
- FastAPI
- SQLAlchemy

# Instalación

- Clone este repositorio a su computadora
- Cree un entorno virtual y activelo
- Instale las dependencias requeridas utilizando el siguiente comando:

# Uso

1. Inicie la aplicación utilizando el siguiente comando:

    uvicorn main:app --reload

2. Abra su navegador web y navegue a la siguiente dirección: 'http://localhost:8000/docs'
3. Utilice la interfaz de usuario de la API de FastAPI para crear, leer, actualizar y eliminar información sobre películas en la base de datos.

# Base de datos

La base de datos utilizada en este proyecto es SQLite. El modelo de la base de datos se define en la carpeta "models" y está gestionado por SQLAlchemy.
