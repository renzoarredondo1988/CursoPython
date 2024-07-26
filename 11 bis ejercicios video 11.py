# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 19:09:38 2022

@author: Crespillo Chiquita
"""

num1=int(input("introduce primer numero, por favor "))

num2=int(input("introduce segundo numero, por favor "))

def devuelveMax(num1,num2):
    
    if num1>num2:
        print(num1)
    elif num2>num1:
        print(num2)
    else:
        print("ambos numeros son iguales")
    

    