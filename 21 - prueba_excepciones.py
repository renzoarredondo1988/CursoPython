# -*- coding: utf-8 -*-


#Las excepciones son un error en tiempo de ejecucion
#El programa esta bien escrito, de sintaxis, etc. pero al correrlo se genera un error
#Esto es, por ej. porque no se puede dividir por 0. La sintaxis es correcta, pero en tiempo de ejecucion se
#genera el error. La solucion ante esto es lo q conoce como "captura o control de excepcion"
#Lo que nos permite controlar una excepcion es que el resto del programa se continue ejecutando
#Cuando corremos el programa, la "pila de llamadas" en la consola nos indica que lineas tienen el error
#y la descripcion y nombre del tipo de error.


def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2
	

op1=(int(input("Introduce el primer número: ")))

op2=(int(input("Introduce el segundo número: ")))		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")