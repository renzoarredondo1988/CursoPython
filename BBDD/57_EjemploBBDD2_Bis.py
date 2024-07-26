#Hacemos la misma base de datos que en el caso anterior, solo que ahora usamos como campo clave
#la funcion autoincrementar, de esta forma evitamos tener que cargar los ID manualmente
#Si agregamos a una de las columnas la accion UNIQUE, lo que hacemos es que en la misma no se pueda repetir
#un elemento. Podria ser util para un DNI por ejemplo

import sqlite3

miConexion=sqlite3.connect("Gestion Productos")

miCursor=miConexion.cursor()

miCursor.execute(''' 
    CREATE TABLE PRODUCTOS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR (20))
    ''')

productos=[
    ("Pelota",20,"Jugueteria"),
    ("Pantalon", 15, "Confeccion"),
    ("Destornillador", 25, "Ferreteria"),
    ("Jarron", 45, "Ceramica")
]

#El valor del campo clave se ingresa con un null
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)",productos)

miConexion.commit()

miConexion.close()