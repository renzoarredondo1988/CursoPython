#Video 19
#Un generador es una estructura que se extrae de una funcion, y se almacena en un objeto iterable (q se puede recorrer)
#Estos valores se almacenan 1 a 1
#Quedan en estado de stand by
#A diferencia de una funcion, es que la funcion retorna todos los valores de una lista.
#El generador, devuelve un valor cuando lo llamemos, luego otro cuando lo volvemos a llamar, y asi (mayor eficiencia)
#El generador tiene de sintaxis de una funcion, solo que en lugar de return lleva un yield

def generaPares1(limite):
    num = 1
    miLista=[]#Creo una lista vacia a la cual se le agregaran pares a medida que se recorra el while
    while num < limite:  # Proponemos un numero limite de 9 numeros pares

        miLista.append( num * 2 ) # agrega valores pares a  la lista

        num = num + 1  # para que traiga al siguiente par

    return miLista

print(generaPares1(5))#Vemos que devuelve una lista completa


#Hacemos un generador que de numeros pares
def generaPares(limite):
    num=1

    while num<limite: #Proponemos un numero limite, cuando el numero par generado supere ese limite finaliza el generador.
        
        yield num*2 #la diferencia a una funcion es q devuelve un yield en lugar de un return
        
        num=num+1 #para que traiga al siguiente par
        
devuelvePares=generaPares(5)

    
print(next(devuelvePares))
    
print("Aqui podria ir mas linea de codigo ")
    
print(next(devuelvePares))#Entre llamada y llamada, el generador queda en lo q se llama estado de suspension
    
print("Aqui podria ir mas linea de codigo ")
    
print(next(devuelvePares))
    
print("Aqui podria ir mas linea de codigo ")


