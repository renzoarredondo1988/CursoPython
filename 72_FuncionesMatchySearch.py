import re

#La funcion match lo que hace es buscar si hay coincidencia al inicio de una cadena de texto
#Distingue entre mayusculas y minusculas

nombre1="Sandra Lopez"

nombre2="Antonio Gomez"

nombre3="sandra Lopez"

if re.match("Sandra",nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

#Con el tercer parametro que admite la funcion match solucionamos el tema de las Mayusculas y min
if re.match("Sandra",nombre3,re.IGNORECASE):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

#Formato para ver coincidencia dentro de una parte de los caracteres
nombre4="Jara Lopez"

nombre5="Antonio Gomez"

nombre6="Lara Lopez"

if re.match(".ara",nombre4):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")

#Con el formato \d podemos verificar si hay un numero o no
cadena1="Jara Lopez"

cadena2="54854855"

cadena3="a54465"

if re.match("\d",cadena3):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")

#La funcion search, a diferencia de la match, busca a lo largo de toda la cadena de caracteres
if re.search("Sandra",nombre1):
    print("Hemos encontrado el nombre")
else:
    print("No lo hemos encontrado")


codigo1="Jara Lopez adsdasdasdsa 71"

codigo2="adasdasdsad71"

codigo3="a54465"

if re.search("71",codigo1):
    print("Hemos encontrado el numero")
else:
    print("No lo hemos encontrado")


#Buscar mas combinaciones en google