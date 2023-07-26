# library_exercise

## Pasos para creación de base de datos
1. Instalar MySQL
2. Ejecutar desde el MySQL Workbrench, el contenido del archivo `query1.sql`

Esto creará la base de datos llamada `library` y las tablas `autor` y `libro`

## Pasos para configurar proyecto de Python
1. El proyecto está en la carpeta `library_app`
2. Crear un Virtual Environment desde la consola, para ello ejecutar:
    ```
    $ python -m venv .env
    ``` 
3. Activar en ambiente creado en el paso #2
    ```
    $ .env\Scripts\activate
    ``` 
4. installar mysql connector
    ```
    $ pip install mysql-connector-python
    ``` 
