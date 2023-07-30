import utils

add_Autor_query = """
INSERT INTO autor 
(nombre, apellido, fecha_nacimiento)
VALUES (%s, %s, %s)
"""

list_Autor_query = """
SELECT * FROM autor 
WHERE nombre = %s"""

get_autor_query = """
SELECT * FROM autor
WHERE id = %s
"""

update_autor_query = """
UPDATE autor
SET nombre = %s, apellido = %s, fecha_nacimiento = %s
WHERE id = %s
"""

list_all_query = """
SELECT * FROM autor
"""

class Autor():

    def __init__(self, id=0, nombre="", apellido="", fecha_nacimiento=None):
        self.id = id
        self.nombre=nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento


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

    def getById(self, cursor, id):
        cursor.execute(get_autor_query, (id, ))
        row = cursor.fetchone()
        if not row:
            return None
        return Autor(row[0], row[1], row[2], row[3])
    
    def update(self, cursor):
        try:
            cursor.execute(update_autor_query, (self.nombre, self.apellido, self.fecha_nacimiento, self.id))
        except Exception as err:
            raise err
        
    def listAll(self, cursor):
        try:
            cursor.execute(list_all_query, ())
            print("Autores:")
            print("ID | NOMBRE | APELLIDO |FECHA DE NACIMIENTO")
            for (id, nombre, apellido, fecha_nacimiento) in cursor:
                print(id, "|", nombre, "|", apellido, "|", fecha_nacimiento)
        except Exception:
            raise
