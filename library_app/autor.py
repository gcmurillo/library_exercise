import utils

add_Autor_query = """
INSERT INTO autor 
(nombre, apellido, fecha_nacimiento)
VALUES (%s, %s, %s)
"""

list_Autor_query = """
SELECT * FROM autor 
WHERE nombre = %s"""


class Autor():

    def __init__(self):
        self.id = 0
        self.nombre = ''
        self.apellido = ''
        self.fecha_nacimiento = None


    def crearAutor(self, cursor):
        print("AGREGAR NUEVO AUTOR")
        try:
            nombre = utils.ingresarString("Ingrese nombre del autor: ")
            apellido = utils.ingresarString("Ingrese apellido del autor: ")
            fecha_nacimiento = utils.ingresarFecha("Ingresar fecha de nacimiento del autor ")
            data_autor = (nombre, apellido, fecha_nacimiento)
            cursor.execute(add_Autor_query, data_autor)
            return True
        except Exception as e:
            print("Error: ", e.__context__)
            return False
    

    def listarAutoresPorNombre(self, cursor, _nombre):
        try:
            rows = 0
            cursor.execute(list_Autor_query, (_nombre, ))
            print("Autores:")
            print("ID | NOMBRE | APELLIDO |FECHA DE NACIMIENTO")
            for (id, nombre, apellido, fecha_nacimiento) in cursor:
                rows += 1
                print(id, "|", nombre, "|", apellido, "|", fecha_nacimiento)
            return rows
        except Exception:
            raise