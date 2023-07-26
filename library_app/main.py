import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'admin',
  'host': '127.0.0.1',
  'database': 'library',
  'raise_on_warnings': True
}

try:
  cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Por favor, verifique que el usuario y contraseña sean correctos!")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("La base de datos no existe!")
  else:
    print(err)
else:
  cnx.close()