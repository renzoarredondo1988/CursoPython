#Video 7
#Las listas son equivalentes a un Array en otros lenguajes
#La sintaxis de las listas es nombre_lista=[elem1,elem2,...]. La ubicacion de cada elemento es el indice
miLista=["Maria","Pepe","renzo","Pampa"]#Sintaxis lista. Los elementos se cuentan desde el indice 0

print(miLista[:]) #Para imprimir todos los valores de una lista se coloca asi
print(miLista[0]) #Imprime el valor del primer elemento, accedemos a traves del indice
#Si imprimis un valor fuera de rango, dara error.
print(miLista[-3])#Valores negativos hace q seleccione el elemento al reves
print(miLista[0:3]) #Imprime porcion de lista, en este caso deja al elemento 3 excluido
print(miLista[:3]) #Se puede excluir el 0 si se arranca desde el principio
print(miLista[2:]) #Lo mismo que el anterior pero al reves
miLista.append("Sandra")#Agrega elemento al final de la lista
print(miLista[:])
miLista.insert(2,"Ana") #Agrega elemento en el indice que querramos
print(miLista[:])
miLista.extend(["Gabriel","Daniel","Coco"])#Une dos listas, en este caso la estamos generando dentro del extend
print(miLista[:])
print(miLista.index("Gabriel"))#Nos indica en que indice se encuentra el elemento. Si hay dos elementos con el
#mismo nombre devolvera el indice del q se encuentre primero
print("Pepe" in miLista) #Para verificar si un elemento se encuentra en la lista. Devuelve T o F
#Las listas pueden tener distintos tipos de elementos
miLista2=[True,5,2.22,"Renzo"]
print(miLista2)
miLista.remove("Ana")#elimina un elemento de una lista
print(miLista[:])
miLista.pop()#Elimina el ultimo elemento de una lista
print(miLista[:])

miLista3=miLista+miLista2
print(miLista3)#Se pueden sumar dos listas para generar una 3ra. no confundir con extends q agrega elementos a una lista
