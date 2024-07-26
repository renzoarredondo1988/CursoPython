import sqlite3

miConexion=sqlite3.connect("Gestion Productos")

miCursor=miConexion.cursor()

#Con la instruccion de abajo leemos la base de datos. en este caso, solo traemos los valores que tengan "Confeccion2
"""
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Confeccion'")

productos=miCursor.fetchall()
print(productos)
"""

"""
#Actualizamos o modificamos un valor dentro de la Tabla
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='Pelota'")
"""

#Con esto eliminamos un valor de la BBDD
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID='4'")
miConexion.commit()

miConexion.close()