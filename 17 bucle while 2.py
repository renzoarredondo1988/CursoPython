
#Hacemos ej. que pregunta la edad. si ponemos negativa vuelve a preguntar
#De esta forma el bucle while funciona indeterminada cantidad de veces

edad=int(input("Introduce la edad, por favor: "))

while edad<5 or edad>100: #El programa se ejecuta infitas veces hasta que se de una edad dentro del rango
    print("Has introducido una edad negativa. Vuelve a intentarlo ")
    edad=int(input("Introduce la edad, por favor: "))
    
print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante "+str(edad))

