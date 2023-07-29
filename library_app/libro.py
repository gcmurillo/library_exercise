import utils
import autor

_autor = autor.Autor()

add_Libro_query = """
INSERT INTO libro
(titulo, fecha_publicacion, autor_id)
VALUES (%s, %s, %s)
"""

search_libro_by_titulo = """
SELECT * FROM libro
WHERE titulo LIKE %s
"""

search_libro_by_autor = """
SELECT l.id, l.titulo, l.fecha_publicacion, l.autor_id, a.nombre, a.apellido 
FROM  libro l
INNER JOIN autor a ON l.autor_id = a.id
WHERE a.apellido LIKE %s
"""

class Libro():

    def listarLibroPorTitulo(self, cursor):
        print("BUSCAR LIBROS POR TITULO")
        try:
            titulo = utils.ingresarString("Ingrese titulo o parte del titulo del libro: ")
            cursor.execute(search_libro_by_titulo, (titulo + "%",))
            print("ID |TITULO | FECHA DE PUBLICACION | ID DEL AUTOR")
            for (id, titulo, fecha_publicacion, autor_id) in cursor:
                print(id, "|", titulo, "|", fecha_publicacion, "|", autor_id)
        except Exception as e:
            print("Error: ", e.__context__)

    def listarLibrosPorAutor(self, cursor):
        print("BUSCAR LIBROS POR AUTOR")
        try:
            apellido_autor = utils.ingresarString("Ingrese apellido del autor: ")
            cursor.execute(search_libro_by_autor, (apellido_autor + "%", ))
            print("LIBRO_ID | TITULO | FECHA DE PUBLICACION | AUTOR_ID | AUTOR")
            for (id, titulo, fecha_publicacion, autor_id, nombre, apellido) in cursor:
                print(id, "|", titulo, "|", fecha_publicacion, "|", autor_id, "|", nombre, apellido)
        except Exception as e:
            print("Error: ", e.__context__)

    def crearLibro(self, cursor):
        print("AGREGAR NUEVO LIBRO")
        try:
            nombre_autor = utils.ingresarString("Ingrese nombre de autor a relacionar: ")
            if _autor.listarAutoresPorNombre(cursor, nombre_autor):
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