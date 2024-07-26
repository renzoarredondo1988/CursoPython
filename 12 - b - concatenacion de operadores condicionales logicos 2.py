# Se pueden agregar todos los operadores qie se deseen

#El ejercicio se analiza si los salarios de una empresa son coherentes

#Comentario: Py es un lenguaje fuertemente tipado (no permite mezclar variables de distinto tipos, por ej,
#para concatenar). Por eso, cuando los valores de salarios ingresados del tipo int se quiere concatenar a
#uno de tipo Str, lo que podemos hacer es ese valor pasarlo a tipo String con la funcion str()
salario_presidente=int(input("introduce salario presidente: "))
print("Salario presidente: "+str(salario_presidente))

salario_director=int(input("introduce salario director: "))
print("Salario director: "+str(salario_director))

salario_jefe_area=int(input("introduce salario jefe de area: "))
print("Salario jefe de area: "+str(salario_jefe_area))

salario_administrativo=int(input("introduce salario administrativo: "))
print("Salario administrativo: "+str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
    print ("Todo funciona correctamente")
else:
    print("Algo anda mal")
    
    