import mysql.connector
from mysql.connector import errorcode
import utils
import autor
import libro

config = {
  'user': 'root',
  'password': 'admin',
  'host': '127.0.0.1',
  'database': 'library',
  'raise_on_warnings': True
}

menu_principal = """
LibraryApp
Menu principal:
1. Agregar nuevo autor
2. Agregar nuevo libro
3. Buscar libro por título
4. Buscar libro por autor
5. Actualizar autor
6. Actualizar libro
7. Eliminar autor
8. Eliminar libro
9. Salir
"""

autor_class=autor.Autor()
libro_class=libro.Libro()

try:
  # Bloque principal
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  # Ciclo principal del programa
  exit = False
  while not exit:
    print(menu_principal)
    input_menu_principal = input("Escoga una opción: ")
    while not utils.validarOpcion(["1", "2", "3", "4", "5", "6", "7", "8", "9"], input_menu_principal):
      input_menu_principal = input("Escoga una opción: ")
    if input_menu_principal == "1": # CREAR AUTOR
      if autor_class.crearAutor(cursor): 
        cnx.commit()
        print("¡Autor agregado correctamente!")
    if input_menu_principal == "2":  # CREAR LIBRO
      if libro_class.crearLibro(cursor):
        cnx.commit()
        print("¡Libro agregado correctamente!")
    if input_menu_principal == "3":  # CONSULTAR POR TITULO
      libro_class.listarLibroPorTitulo(cursor)
    if input_menu_principal == "4":  # CONSULTAR POR AUTOR
      libro_class.listarLibrosPorAutor(cursor)
    if input_menu_principal == "5":  # ACTUALIZAR AUTOR
      print("ACTUALIZAR AUTOR")
      _nombre = utils.ingresarString("Ingrese nombre del autor: ")
      autor_class.listarAutoresPorNombre(cursor, _nombre)
      _id = utils.ingresarString("Ingrese el ID del autor a editar: ")
      _autor = autor_class.getById(cursor, _id)
      if autor:
        _autor.nombre = utils.ingresarString("Ingrese nuevo nombre (anterior: %s): " % _autor.nombre)
        _autor.apellido = utils.ingresarString("Ingrese nuevo apellido (anterior: %s): " % _autor.apellido)
        _autor.fecha_nacimiento = utils.ingresarFecha("Ingrese nueva fecha de nacimiento (anterior: %s): " % _autor.fecha_nacimiento)
        try:
          _autor.update(cursor)
          cnx.commit()
          print("¡Autor actualizado!")
        except Exception as err:
          print("Error: ", err)
      else:
        print("No se encontró autor con id: %s" % _id)
    if input_menu_principal == "6":  # ACTUALIZAR LIBRO
      print("ACTUALIZAR LIBRO")
      try: 
        _titulo = utils.ingresarString("Ingrese título del libro: ")
        libro_class.listarLibroPorTitulo(cursor, _titulo)
        _id = utils.ingresarString("Ingrese ID del libro a editar: ")
        _libro = libro_class.getById(cursor, _id)
        if _libro:
          _libro.titulo = utils.ingresarString("Ingrese nuevo nombre (anterior: %s): " % _libro.titulo)
          _libro.fecha_publicacion = utils.ingresarFecha("Ingrese nueva fecha de publicacion (anterior: %s): " % _libro.fecha_publicacion)
          autor_class.listAll(cursor)
          _libro.autor_id = utils.ingresarString("Ingresa ID del nuevo autor (anterior: %s): " % _libro.autor_id)
          _libro.update(cursor)
          cnx.commit()
          print("¡Libro actualizado!")
        else:
          print("No se encontró libro con id: %s" % _id)
      except Exception as err:
        print("Error: ", err.__context__)
    if input_menu_principal == "7": # ELIMINAR AUTOR
      print("ELIMINAR AUTOR")
      _nombre = utils.ingresarString("Ingrese nombre del autor: ")
      autor_class.listarAutoresPorNombre(cursor, _nombre)
      _id = utils.ingresarString("Ingrese el ID del autor a eliminar: ")
      _autor = autor_class.getById(cursor, _id)
      if autor:
        try:
          confirm = utils.ingresarString("Ingrese (Y) para confirmar la eliminación del autor %s %s: " % (_autor.nombre, _autor.apellido))
          if confirm == "Y":
            _autor.delete(cursor)
            cnx.commit()
            print("¡Autor eliminado!")
          else:
            print("No se elimina al autor")
        except Exception as err:
          print("Error: ", err)
      else:
        print("No se encontró autor con id: %s" % _id)
    if input_menu_principal == "8": # ELIMINAR LIBRO
      print("ELIMINAR LIBRO")
      try: 
        _titulo = utils.ingresarString("Ingrese título del libro: ")
        libro_class.listarLibroPorTitulo(cursor, _titulo)
        _id = utils.ingresarString("Ingrese ID del libro a eliminar: ")
        _libro = libro_class.getById(cursor, _id)
        if _libro:
          try:
            confirm = utils.ingresarString("Ingrese (Y) para confirmar la eliminación del libro %s: " % _libro.titulo)
            if confirm == "Y":
              _libro.delete(cursor)
              cnx.commit()
              print("¡Libro eliminado!")
            else:
              print("No se elimina el libro")
          except Exception as err:
            print("Error: ", err.__context__)
        else:
          print("No se encontró libro con id: %s" % _id)
      except Exception as err:
        print("Error: ", err.__context__)
    if input_menu_principal == "9": 
      cursor.close()
      cnx.close()
      print("Hasta luego!")
      exit = "5"


except mysql.connector.Error as err:
  # Errores al conectar a la base de datos
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Por favor, verifique que el usuario y contraseña sean correctos!")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("La base de datos no existe!")
  else:
    print(err)
else:
  cnx.close()