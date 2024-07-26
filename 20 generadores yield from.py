#Video 20

#Utilidad: simplificar el codigo de los generadores en el caso de bucles anidados

#Creamos una funcion generador que devuelve un conjunto de ciudades
def devuelve_ciudades(*ciudades):#cuando agregamos un asterisco antes del argumento significa que va a recibir
    #un numero indeterminado de elementos, y los mismos seran en forma de tupla
    for elemento in ciudades:
       # yield elemento #me devuelve los elementos dentro, como Madrid, Barcelona, etc
       yield from elemento #me devuelve subelementos, es decir, las letras que forman a los elementos
        
ciudades_devueltas=devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))