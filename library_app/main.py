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
5. Salir
"""

try:
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  # Ciclo principal del programa
  exit = False
  while not exit:
    print(menu_principal)
    input_menu_principal = input("Escoga una opción: ")
    while not utils.validarOpcion(["1", "2", "3", "4", "5"], input_menu_principal):
      input_menu_principal = input("Escoga una opción: ")
    if input_menu_principal == "1":
      if autor.crearAutor(cursor): 
        cnx.commit()
        print("¡Autor agregado correctamente!")
    if input_menu_principal == "2":
      if libro.crearLibro(cursor):
        cnx.commit()
        print("¡Libro agregado correctamente!")
    if input_menu_principal == "5": 
      cursor.close()
      cnx.close()
      print("Hasta luego!")
      exit = "5"


except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Por favor, verifique que el usuario y contraseña sean correctos!")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("La base de datos no existe!")
  else:
    print(err)
else:
  cnx.close()