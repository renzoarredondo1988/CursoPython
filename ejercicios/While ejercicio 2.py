# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:24:59 2022

@author: Crespillo Chiquita
"""

numero=int(input("Introduce un numero, por favor "))
contador=1

while numero>=0:
    numero=int(input("Introduce un nuevo numero, por favor "))
    contador=contador+1
    
    
if numero<0:
    print("Introdujiste un numero negativo, el programa ha finalizado. La cantidad de intentos fue de "+str(contador))
