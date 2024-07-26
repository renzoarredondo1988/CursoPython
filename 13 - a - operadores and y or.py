#Video 13

#Hacemos ejercicio en donde se entrega una beca en funcion de 3 variables
#Distancia, hermanos, salario. Tiene que cumplir con los 3 requisitos
#El condicional and se puede por reemplazar por "y si ademas"

print("Programa de becas año 2022")
distancia_escuela=int (input("introduce la distancia a la escuela en km"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el n° de hermanos en el centro"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:#Con los and establecemos que te
    #tengan que dar todas las condiciones. Si en lugar del and hubiera un or, estariamos diciendo que si no
    #se cumple una condicion o la otra, tendra derecho a beca. Se pueden concatenar todos los que se quieran
    print("Tienes derecho a beca")
else:#Con que una condicion no se cumpla, ira al else
        print("No tienes derecho a beca")
