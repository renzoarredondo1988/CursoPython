# -*- coding: utf-8 -*-
"""

"""
"""
#La instruccion Raise lo que nos permite es "lanzar" una excepcion, es decir, indicarle al programa que ante
#cierta situacion se produce un error y no se siga corriendo el mismo
#Con esto solo probamos usar la instruccion Raise. Como vemos, no se puede tener una edad menor que 0
#Entonces "creamos" la excepcion con la instruccion raise
def EvaluaEdad(edad):
    if edad>0:
        raise TypeError("no se permiten edades negativas")
    if edad<20:
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<60:
        return "eres maduro"
    elif edad<100:
        return "cuidate"
    
print(EvaluaEdad(70))
"""

import math



def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
            return math.sqrt(num1)

op1=(int(input("Introduce un numero ")))

try:
    print(calculaRaiz(op1))
#Capturamos el error que nosotros mismo generamos con el raise (ValueError)
except ValueError as ErrorDeNumeroNegativo:#Le damos un nombre o alias a ese error
    print(ErrorDeNumeroNegativo)#Al imprimir este error lo que estamos haciendo es imprimir lo que escribimos
    #dentro del parametro del error referenciado
print("Programa terminado")