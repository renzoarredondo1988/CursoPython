import sqlite3

#Pasos a seguir para interactuar con una base de datos
#Abrir - crear conexion, crear puntero, ejecutar query(consulta) SQL, manejar los resultados de la Query
#(Create, Read, Update, Delete), Cerrar puntero, Cerrar Conexion

miConexion=sqlite3.connect("Primera base")

miCursor=miConexion.cursor()

#Creamos una tabla que contiene columnas con el tipo de articulo, precio y seccion
miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER,SECCION VARCHAR(20))")

#Insertamos a la tabla una fila con parametros
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON',15,'DEPORTES')") #Inserta valores

#Hacemos una lista con tuplas para ingresar varios productos de una sola vez
"""variosProductos=[
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos) #Con el metodo executemany lo que hacemos
#es ingresar una tupla con varios valores. El (?,?,?) lleva tantas posiciones o "?" como cantidad de columnas o parametros
#deba ingresar, en este caso la tabla tiene 3 posiciones de valores (Producto, precio y seccion)
"""

miCursor.execute("SELECT * FROM PRODUCTOS")#Con el select * seleccionamos todos los elementos de la lista productos

variosProductos=miCursor.fetchall() #Con el metodo fetcall lo que hacemos es almacenar los valores de la BBDD seleccionados
#y almacenarlos en una lista llamada variosProductos

print(variosProductos)

#Con un bucle for podemos imprimir las tuplas fuera de la lista
for productos in variosProductos:
    print(productos)

for productos in variosProductos:
    print("Articulo ",productos[0]," Seccion: ",productos[2])

miConexion.commit() #confirma los cambios realizados

miConexion.close()