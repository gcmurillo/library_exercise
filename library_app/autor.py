import utils

add_Autor_query = """
INSERT INTO autor 
(nombre, apellido, fecha_nacimiento)
VALUES (%s, %s, %s)
"""

def crearAutor(cursor):
    print("CREAR AUTOR")
    try:
        nombre = utils.ingresarString("Ingrese nombre del autor: ")
        apellido = utils.ingresarString("Ingrese apellido del autor: ")
        fecha_nacimiento = utils.ingresarFecha("Ingresar fecha de nacimiento del autor ")
        data_autor = (nombre, apellido, fecha_nacimiento)
        cursor.execute(add_Autor_query, data_autor)
        return True
    except Exception as e:
        print("Error")
        return False
    
