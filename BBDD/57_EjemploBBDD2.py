import sqlite3

miConexion=sqlite3.connect("Gestion Productos")

miCursor=miConexion.cursor()

"""
#Con la triple comilla simple lo que permite es crear todo en diferentes renglones
miCursor.execute(''' 
    CREATE TABLE PRODUCTOS(
    CODIGO_ARCHIVO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR (20))
    ''')

#Vemis que el codigo_archivo es el primary key o campo clave. Es, basicamente, un valor unico que identifica a cada campo
#basicamente, un ID
productos=[
    ("AR01","Pelota",20,"Jugueteria"),
    ("AR02", "Pantalon", 15, "Confeccion"),
    ("AR03", "Destornillador", 25, "Ferreteria"),
    ("AR04", "Jarron", 45, "Ceramica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",productos)
"""
"""
#Agregamos otro producto
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05','Tren',15,'Jugueteria')")
miConexion.commit()
"""
"""
#Vemos que si queremos agregar un articulo con el mismo valor de campo clave arroja error
miCursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03','Tren',15,'Jugueteria')")
miConexion.commit()
"""



miConexion.close()