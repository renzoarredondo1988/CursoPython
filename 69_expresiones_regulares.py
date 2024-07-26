#Expresiones regulares o regex. Lo q permite es hacer una busca de caracteres que coincidan

import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla"

textoBuscar="Python"

#Verificamos con un condicional si un texto esta dentro de una cadena
"""if re.search(textoBuscar,cadena) is not None:
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

print(re.search("aprender",cadena))"""

textoEncontrado=re.search(textoBuscar,cadena)

print(textoEncontrado.start())

print(textoEncontrado.end())

print(textoEncontrado.span())

print(len(re.findall(textoBuscar,cadena)))

lista_nombres=['http://pildorasinformaticas.es','ftp://pildorasinformaticas.es','http://pildorasinformaticas.com',
    'ftp://pildorasinformaticas.com',
    'Ana Gomez','Maria Martin','Sandra Lopez','Sandra Fernandez']

for elemento in lista_nombres:
    if re.findall('^Sandra',elemento):#^ este simbolo se utiliza para decir aquellos valores de listas de caracteres que comienzan por:
        print(elemento)

for elemento in lista_nombres:
    if re.findall('Martin$',elemento):#$ este simbolo se utiliza para decir aquellos valores de la lista que terminen por:
        print(elemento)

for elemento in lista_nombres:
    if re.findall('.es$',elemento):#$ este simbolo se utiliza para decir aquellos valores de la lista que terminen por:
        print(elemento)


lista_nombres2=['http://informaticaenespaña.es','ftp://pildorasinformaticas.es','http://pildorasinformaticas.com']

for elemento in lista_nombres2:
    if re.findall('[ñ]',elemento):#[] este simbolo se utiliza para decir aquellos valores de la lista que contienen:
        print(elemento)

lista_nombres3=["Hombres","Mujeres","Niños","Niñas"]

for elemento in lista_nombres3:
    if re.findall('Niñ[oa]s',elemento):#[] segun lo que se encierra puede ser la combinacion de una u otra
        print(elemento)


#Manejo de rangos. Podemos encerrar y traer aquellos elementos que contengan caracteres q esten comprendidos entre un rango de lentras
lista_nombres4=["Ana","Pedro","Maria","Rosa","Sandra","Celia"]

for elemento in lista_nombres4:
    if re.findall('[o-t]',elemento):#[] segun lo que se encierra puede ser la combinacion de una u otra
        print(elemento)

lista_nombres5=["Ma1","Se1","Ma2","Ba1","Ma3","Va1","Va2","Ma4","MaA","MaB","MaC"]

for elemento in lista_nombres5:
    if re.findall('^Ma[0-3]',elemento):#^ En este caso, la casita niega, serian "valores q no contengan del 1 al 3"
        print(elemento)

for elemento in lista_nombres5:
    if re.findall('Ma[0-3A-B]',elemento):#^ En este caso, la casita niega, serian "valores q no contengan del 1 al 3"
        print(elemento)