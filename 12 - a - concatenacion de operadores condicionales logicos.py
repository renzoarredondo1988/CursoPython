#Video 12
#Python no tiene el condicional switch (como en Java), pero si tiene otras opciones como el de
#concatenar operadores logicos para definir rangos


edad=-7

if 0<edad<100: #concatenacion de operador < para determinar si un valor esta dentro de un rango abreviando codigo
    #ya que se podria hacer con condicionales if, elif, else.
    #El flujo de ejecucion lo que hace es evaluar de izquierda a derecha. Si 0 es menor que edad, avanza preguntandose
    #si edad es <100. Si no se diera alguno de los casos, se iria al else.
    print("Edad es correcta")
else:
    print("Edad incorrecta")
    
    