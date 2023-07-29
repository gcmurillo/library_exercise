import utils
import autor

add_Libro_query = """
INSERT INTO libro
(titulo, fecha_publicacion, autor_id)
VALUES (%s, %s, %s)
"""

def crearLibro(cursor):
    print("AGREGAR NUEVO LIBRO")
    try:
        nombre_autor = utils.ingresarString("Ingrese nombre de autor a relacionar: ")
        if autor.listarAutoresPorNombre(cursor, nombre_autor):
            autor_id = utils.ingresarString("Ingrese ID del autor del libro: ")
            titulo = utils.ingresarString("Ingrese título del libro: ")
            fecha_publcacion = utils.ingresarFecha("Ingrese fecha de publicación ")
            data_libro = (titulo, fecha_publcacion, autor_id)
            cursor.execute(add_Libro_query, data_libro)
            return True
        else:
            print("No se encuentran coincidencias para %s, por favor, intente nuevamente o cree el autor" % nombre_autor)
        return False
    except Exception as e:
        print("Error: ", e.__context__)
        return False