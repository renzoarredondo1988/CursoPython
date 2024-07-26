# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 18:51:57 2022

@author: Crespillo Chiquita
"""

nota_alumno=int(input("Introduce tu nota, por favor"))

if nota_alumno<5:
    print("Insuficiente")

elif nota_alumno<7:
    print("Regular")    

elif nota_alumno<8:
    print("Bien")

elif nota_alumno<9:
    print("Sobresaliente") 
    
else:
    print("Excelente")