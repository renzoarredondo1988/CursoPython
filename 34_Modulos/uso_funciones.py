import funciones_matematicas #Para importar un modulo en Py se usa esta nomenclatura (import nombre_modulo)

from funciones_matematicas import * #De esta forma podemos traer una funcion del modulo y reducir la escritura
#del mismo al llamar la funcion. Si ponemos un asterisco llamamos a todas las funciones que contiene el modulo

funciones_matematicas.sumar(7,5) #Para hacer uso de una funcion del modulo nombre_modulo.nombrefuncion

funciones_matematicas.restar(7,5) #Vemos que se vuelve engorroso esta metodologia

sumar(3,5) #ejemplo reducido al importar con from

restar(4,2)