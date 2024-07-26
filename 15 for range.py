

#nos da un rango de valores, desde el 0 al 5 incluido.
for i in range(5):
    print(f"valor de la variable {i}")#La f es una funcion especial, que permite concatenar.

print("nuevo bucle for")
for i in range(5,10):#Incluye al 5 pero no al 10
    print(f"valor de la variable {i}")

print("nuevo bucle for")
#El range permite analizar un elemento dentro de un rango, y determinando un salto
for i in range(5,25,5):
    print(f"valor de la variable {i}")
    
    