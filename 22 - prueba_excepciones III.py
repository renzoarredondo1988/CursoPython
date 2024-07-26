# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 13:25:12 2023

@author: Crespillo Chiquita
"""
#En este caso, si no ponemos las excepciones, tenemos dos tipos de errores dentro de la funcion
#Dividir por 0 y poner Strings y otro tipo de valor en lugar de numeros
def divide():
    
    try:
    
        opc1=(float(input("introduce el primer numero: ")))
    
        opc2=(float(input("introduce el segundo numero: ")))
    
        print("La division es: "+str(opc1/opc2))
        
    except ValueError:#Captura el error por Valor
        print("El valor introducido es erroneo")
    
    except ZeroDivisionError:#Captura el error por 0.
    #Vemos que con un try, podemos poner dos excepciones o las que fueran necesarias
    #Se podria poner un except sin ninguna descripcion del error, pero no es recomendado ya que el programa
    #seguiria funcionando, pero el usuario no podria identificar cual es el error que esta sucediendo (Ver mas abajo)
        print("no se puede dividir por 0!")

    finally:
         print("Calculo finalizado")#El bloque finally lo que hace es que su bloque se ejecute siemproe, por mas
        #que haya error o no, e incluso si se prescindiera del except
    
divide()


#Con el except solo

"""
def divide():
    
    try:
    
        opc1=(float(input("introduce el primer numero: ")))
    
        opc2=(float(input("introduce el segundo numero: ")))
    
        print("La division es: "+str(opc1/opc2))
        
    except:
        ("Se ha producido un error")
    
    print("Calculo finalizado")
    
divide()

"""