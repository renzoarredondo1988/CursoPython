import pickle

lista_nombres=["Pedro","Ana","Maria","Isabel"]

fichero_binario=open("lista_nombres","wb")#Con la clase pickle lo que podemos hacer es un objeto, lista,etc.
#Pasarlo a un fichero en codigo binario, lo que facilita su lectura desde cualquier pc
#lista_nombres sera el nombre del fichero, fichero_binario es el fichero en memoria

pickle.dump(lista_nombres,fichero_binario)#Con este paso, el fichero quedara guardado en nuestro directorio

fichero_binario.close() #Ya se puede cerrar el fichero en memoria, e incluso se puede eliminar

del (fichero_binario)