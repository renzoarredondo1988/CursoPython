#Video 9 - Diccionarios

#Los diccionarios se hacen a traves de una clave:valor
#Las claves pueden ser de cualquier tipo: Texto, numero, tupla

miDiccionario={"Alemania":"Berlin","Francia":"Paris","España":"Madrid","Argentina":"Buenos Aires"}#Sintaxis
print(miDiccionario["Francia"])#Llamada al diccionario a traves de la clave, y devuelve el valor
print(miDiccionario)#Accedemos al diccionario entero

miDiccionario["Italia"]="Lisboa" #Agrego un elemento mas a un diic
print(miDiccionario)

miDiccionario["Italia"]="Roma" #Corrijo parametro asignado. Se sobreescribe. Lo que no pueden haber dos claves iguales
print(miDiccionario)

del miDiccionario["Argentina"]#Eliminar elemento del dicc, se hace con la clave
print(miDiccionario)

miDiccionario2={"Peru":"Lima",23:"Escocia","Mosqueteros":3}#Los dicc permiten claves y valor de disntintos tipos
print(miDiccionario2)

miTupla=["España","Francia","Reino Unido"]
miDiccionario3={miTupla[0]:"Madrid",miTupla[1]:"Paris",miTupla[2]:"Londres"}#Usamos tuplas dentro de un dicc
print(miDiccionario3)

#Uso una tupla como un valor. Lo metemos dentro de un subdiccionario, es decir el valor es un dicc
#que dentro, a su vez, tiene una tupla
miDiccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1992,1993,1996,1997]}}
print(miDiccionario4)

print(miDiccionario4.keys)#Imprime las claves
print(miDiccionario4.values())#Imprime los valores
print(len(miDiccionario4))#Imprime la cantidad de valores