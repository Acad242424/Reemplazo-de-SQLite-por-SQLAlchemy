# Biblioteca Personal — MariaDB + SQLAlchemy

## Instalación de MariaDB

mysql -u root -p

CREATE DATABASE biblioteca;

## Configuración en database.py

DB_USER = "usuario"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_NAME = "biblioteca"

## Instalar dependencias

pip install -r requirements.txt

## Ejecutar aplicación

python app.py
