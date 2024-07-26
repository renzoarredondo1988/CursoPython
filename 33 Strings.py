nombreUsuario=input("Introduce tu nombre de usuario ")
print("El nombre es ",nombreUsuario.upper())#todo en mayuscula

print("El nombre es ",nombreUsuario.lower())#todo en minuscula

print("El nombre es ",nombreUsuario.capitalize())#Primera letra en mayuscula

edad=input("Introduce la edad ")
print(edad.isdigit())#Indica si es un String o no

#Con un bucle while, verificamos con el edad.isdigit si es un string o un numero.
#Mientras sea un string, quedara trabado en el while, cuando se coloque un numero, sale del bucle (o no ingresa)
#y verifica el condicional
while(edad.isdigit()==False):
    print("Introduce un valor numerico ")
    edad = input("Introduce la edad ")

if(int(edad)<18): #En py todo lo q ingresamos pro consola es un Str, por eso usamos la funcion int
    print("No puedes pasar")
else:
    print("Puedes pasar")