# -*- coding: utf-8 -*-
#correccion del error ZeroDivisionError
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):
    try:#La instruccion que es susceptible que cometa el error la tenemos que meter dentro de un bloque try except
        return num1/num2
    except ZeroDivisionError:#except con la descripcion del error que nos dio la consola,sino el error continuara
         print("No se puede dividir entre 0")#dentro del bloque de la excepcion, ponemos lo que queremos q haga el programa
         return "Operacion erronea"
     
        
while True:
    
    try:
        op1=(int(input("Introduce el primer número: ")))

        op2=(int(input("Introduce el segundo número: ")))	
    
        break

    except ValueError:
        print("Los valores introducidos no son correctos")	
	
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