# -*- coding: utf-8 -*-

#Continuamos arreglando el error del video anterior (ValueError)
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
         print("No se puede dividir entre 0")
         return "Operacion erronea"
     
        
while True: #el try except lo ponemos dentro de un bloque While, porque sino, el programa continuaria corriendo
    #pero sin poder darle valores a op1 y/o op2, lo que arrojaria otro tipo de error cuando se solicite la operacion
    #a ejecutar (suma, resta, etc). La solucion con el While es que nos pide que demos los valores numericos para
    #poder salir del bucle
    #Generamos otro bloque try Except en donde se genera el error de Value
    try:#El try le indica al programa que intente correr el codigo
        op1=(int(input("Introduce el primer número: ")))

        op2=(int(input("Introduce el segundo número: ")))	
    
        break #Cuando los valores de op1 y op2 sean correctos, saldra del while gracias al break, sin leer el except
        #mientras tanto, nos solicitara los valores permanentemente hasta ingresarlos bien y asi poder salir del bucle

    except ValueError:#El except da la excepcion al error, luego, el bloque donde indicamos que queremos que haga
        print("Los valores introducidos no son correctos. Intentalo de nuevo")	
	#Solo podemos salir del bucle While hasta que llegue el break


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