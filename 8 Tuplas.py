#Video 8
#Las tuplas son listas inmutables. Es decir, listas q no se pueden modificar.
#Tienen ciertas restricciones como que no se puede agregar, eliminar elementos, etc.
#Las tuplas son mas rapidas, pueden utilizarse como claves en los diccionarios (las listas no)
#La sintaxis y propiedades son iguales, nada mas q es nombreTupla=(elem1,elem2,etc)

miTupla=("Juan",3,1,1995)#Sintaxis Tupla, permite variables diferentes
print(miTupla)
print(miTupla[0])

miLista=list(miTupla)#Convertimos una tupla en lista
print(miLista)

miTupla2=tuple(miLista)#Proceso inverso, convertimos lista en tupla
print(miTupla2)

print("Juan" in miTupla)#Ver si esta el elemento en la tupla
print(miTupla.count(3))#Cuento cuantas veces se encuentra ese elemento dentro de la tupla

print(len(miTupla))#Cuenta la cantidad de elementos contiene una tupla

miTupla3=("Renzo",)#Tupla unitaria, tupla de un solo elemento, se tiene que poner la ","
print(miTupla3)

nombre,dia,mes,agno=miTupla #Desempaquetado de tupla. Asigno una variable a cada valor de una tupla
print(nombre)
print(dia)
print(mes)
print(agno)