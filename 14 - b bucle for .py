
#Con un contador, analizamos q haya @ y . .
#Obviamente que este programa no es del todo correcto, porque podrian haber dos @ y no puntos.
contador=0
miEmail=input("Introduce tu direccion de email: ")


for i in miEmail:
    if(i=="@" or i=="."):
        contador=contador+1
        
if contador==2:
    print("Email es correcto")
else:
    print("Email no es correcto")