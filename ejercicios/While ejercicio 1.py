# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:08:14 2022

@author: Crespillo Chiquita
"""

numero_ref=int(input("Introduce un numero, por favor "))
numero_posterior=int(input("Introduce un numero, poor favor "))

while numero_ref<numero_posterior:
    
    numero_ref=numero_posterior
    
    numero_posterior=int(input("Introduce otro numero, por favor "))
    

if numero_ref>numero_posterior:
        print("El numero es menor al anterior. El Programa finalizo")
        
    
        
    