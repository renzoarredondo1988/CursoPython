# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 20:35:31 2022

@author: Crespillo Chiquita
"""

#Ejercicio 3

contador_arroba=0
contador_punto=0

email=input("Escribe tu direccion de email ")

for i in email:
    if i=="@":
        contador_arroba=contador_arroba+1
       
    if i==".":
        contador_punto=contador_punto+1
        
print (contador_arroba)
print (contador_punto)
        
if contador_arroba==1 and contador_punto>0:
    print("Correo valido")
else:
    print("Correo invalido")
        
    