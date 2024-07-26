# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 19:26:48 2022

@author: Crespillo Chiquita
"""

#Ejercicio 2

password=input("Introduce una contraseña, por favor ")
validacion=True


for i in password:
    if i==" " or len(password)<8:
        validacion=False
        
if validacion==False:    
   print("La contraseña es incorrecta")
else:
        print("La contraseña es correcta")