
#Video 10
#Condicional if, si es V, lee el codigo, sino, continua

print("Programa de evalacuion de notas de alumnos")

nota_alumno=input("Introduce la nota del alumno: ") #creo una variable que nos va a permitir dar un valor por teclado (consola)

#Ambito de una variable: una variable solo se puede utilizar dentro del ambito donde se asigne.
#Si se hace dentro de una funcion, solo sera utilizable dentro de dicha funcion
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5: #El bloque if solo se ejecutara siempre que sea cierto
        valoracion="suspenso" #fijarse la identacion para ver que esta y que no dentro del condicional
    return valoracion

#print(evaluacion(nota_alumno)) #El valor ingresado por consola Python lo toma como un String, por eso tira error
print(evaluacion(int(nota_alumno)))#con la funcion int, hacemos que el valor q ingresamos x consola se transforme en int