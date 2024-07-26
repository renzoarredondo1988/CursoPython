
#Video 18

#La instruccion continue lo que hace es saltar ese giro del bucle



#En el primer bucle, vemos que cuando imprimimos la variable letra, muestra todas las letras
for letra in "Python":
    print("Viendo la letra "+letra)

print(" ")

#En este bucle, vemos que cuando recorre la palabra Python, cuando se encuentre con la letra h, de continue,
#Es decir, ignora todo lo que contunua debajo del cuerpo del bucle que le sigue, continuando con la siguiente
#iteracion
for letra in "Python":
    if letra=="h":
        continue
    print("Viendo la letra "+letra)

print(" ")


#Hacemos ejercicio de contar letras, no caracteres, es decir sin espacios en blanco, de lo aprendido anteriormente
contador=0
nombre="Pildoras informaticas"
for i in nombre:
        if i==" ":
            continue
        contador+=1 #El +=1 es lo mismo que decir contador=contador+1
    
    
    
print(contador)

    
    