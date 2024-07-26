
#Video 11 if_else
#else se puede reemplazar en "y si no es verdad"


edad_usuario=int(input("Introduce tu edad, por favor: "))

#Analizamos si un usuario puede entrar a un lugar segun su edad
#si solo ponemos un if, al no cumplirse la condicion  nos quedaria erroneo
#cada else debe ir acompañado de su respectivo if. No puede haber else sin if.
#si se cumple el if, el programa ignora el else, y viceversa.
#No puede haber dos else para un solo if. Si hubiera varios if, el else va acompañado del if mas cercano
#Por eso cuando se tienen que evaluar varias condiciones, se utiliza con un elif
#En este caso, entra en el else cuando no se cumpla ninguna de las condiciones colocadas entre el if y los elif

if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")
    
print("El programa ha finalizado")