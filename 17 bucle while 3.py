
import math

#Crearemos un programa que halle la raiz cuadrada de un numero

print ("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))

intentos=0

while numero<0:#Si el numero es mayor que 0, no entra en el bucle while
    print("No se puede hallar la raiz de un numero negativo")
    
    if intentos==2:#Analiza la cantidad de intentos, si llega a 2 sale del programa. Primero ingresa con 0 intentos, luego con 1, y al 2do salge
        print("Has consumido demasiados intentos. El programa ha finalizado ")
        break;#la instruccion break sale del bucle
        
    numero=int(input("Introduce un numero por favor: "))#Como pusimos un valor negativo, entro al bucle y solicito que ingresemos otro numero
    if numero<0:#Si nuevamente pusimos un valor menor q 0, ingresa a este condicional,sino, saldra del bucle, porque no se cumplira la condicion while
        intentos=intentos+1#si nuevamente se puso un valor menor q 0, intentos tomara un valor de 1, luego de 2, y sale del while.
    
if intentos<2:#La solucion solo se dara si los intentos fueron menor a 2, es decir, se ingreso 3 valores
    solucion=math.sqrt(numero)
    print ("La raiz cuadrada de "+str(numero)+" es "+str(solucion))