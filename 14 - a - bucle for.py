#Video 14

#El bucle determinado se sabe a priori cuantas veces se va a ejecutar el codigo dentro de el
#sintaxis for variable in elemento_a_recorrer

for i in ["primavera","verano","otoño","invierno"]: #sintaxis - declaracion del bucle
    print(i)#Cuerpo del bucle. Puede ser una linea o varias, siempre con la identacion correspondiente
    #Aca la variable i va a tomando los valores dentro de la lista, cada vez que recorre el cuerpo, la variable
    #cabia al elemento siguiente

for i in [1,2,3]: #Ojo aca. Se imprime 3 veces hola porque el bucle tiene 3 elemenos, es decir, i va a tomar
    print("Hola")#3 valores, y va a recorrer el cuerpo del bucle 3 veces

print("Nuevo bucle")
for i in [1,2,3,55]: #Ojo aca. Se imprime 3 veces hola porque el bucle tiene 3 elemenos, es decir, i va a tomar
    print("Hola")#3 valores, y va a recorrer el cuerpo del bucle 3 veces
