
#Operador in. Vamos a suponer que un alumno tiene que elegir una asignatura optativa
#Si o si tiene que estar contemplada en el listado de posibles
#Con el operador in lo que hacemos es indicar si un valor se encuentra o no dentro de las opciones

print("Asignaturas optativas Año 2017")
print("Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input(("Escribie la asignatura escogida: "))

asignatura=opcion.lower()

#Con la linea de arriba, lo que hago es que independientemente de si el alumno escriba en mayuscula o
#minuscula, lo pasa todo a minuscula. Entonces en el in pongo todo en minuscula y no le erro nunca
#Py es Case Sensitive (distingue entre mayuscula y minuscula


if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida "+asignatura)
else:
    print("La asignatura escogida no esta contemplada")

    