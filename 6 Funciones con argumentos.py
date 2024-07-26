#Video 6

#Paso se parametros en una funcion

"""def suma():
    num1=5  #Esta funcion tiene el problema que siempre me deja sumar los mismos valores
    num2=7   #Si agregamos argumentos a la funcion podemos aumentar su potencialidad
    print(num1+num2) """

def suma(num1,num2):
    print(num1+num2)

suma(100,200) #Cuando la funcion tiene parametros,al llamarla, debemos hacerlo ingresando la cantidad q correspondan
suma(2,35) #los valores se almacenan en el parametro que corresponda. Ej. num1=2 num2=35

"""almacena=suma() #Al no haber return, no puedo almacenar el valor que devuelve la funcion en una variable
print (almacena)"""
#Funcion con retorno. Comparable con maquina expendedora, que segun los parametros q ingresas es lo q devuelve

def suma2(num3,num4):
    resultado=num3+num4
    return resultado

suma2(5,10) #Si lo dejamos asi, no devolvera nada, pero si funciona, nada mas q no estamos imprimiendo
print(suma2(5,10)) #Con el print le estamos diciendo que imprima lo q devuelva la funcion suma2 (imprime el return)

almacena_resultado=suma2(5,8) #La ventaja del return es que nos permite almacenar lo q devuelve la funcion
print("El valor de almacena_resultado es", almacena_resultado) #en una varuable
