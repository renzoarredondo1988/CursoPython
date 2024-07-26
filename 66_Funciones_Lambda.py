
#La funcion lamba permite resumir una funcion sencilla aun mas
#No siempre es posible resumir una funcion en otra lambda
"""def area_triangulo(base,altura):
    return (base*altura/2)

print(area_triangulo(7,5))"""

area_triangulo=lambda base,altura:(base*altura/2)

print(area_triangulo(7,5))

al_cubo=lambda numero:(numero**3)

print(al_cubo(13))

destacarValor=lambda comision:"¡{}$!".format(comision)

comisionAna=15855

print(destacarValor(comisionAna))


