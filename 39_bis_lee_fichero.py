import pickle

fichero=open("lista_nombres","rb")#leemos el archivo que creamos en 39_trabajo_serializacion
#en open se agrega el nombre del archivo, rb es read binarie

lista=pickle.load(fichero)
print(lista)

#De esta forma vemos que creamos una lista, la pasamos a codigo binario, luego de codigo binario la trajimos
#nuevamente a nuestro programa Py y la pudimos leer nuevamente