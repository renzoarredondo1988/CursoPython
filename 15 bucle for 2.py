#Video 15

for i in ["Pildoras","Informaticas",3]:
    print(i,end=" ")#Con el end= lo que hacemos es que me imprima sin salto de linea cada recorrido del bucle

for i in "renzo.mau1988@gmail.com":
    print(i) #toma al String letra x letra


#Esta situacion me permite analizar si al escribir un correo tiene el @ escrito, como algo necesario si o si
email=False #Un solo = asigna un valor a una variable. Dos iguales "==" compara.
miEmail=input("Introduce tu direccion de email: ")


for i in miEmail:
    if(i=="@"): #Si no existe el @, se mantendra la condicion de email=False, por lo que nunca entra ene l condicional
        email=True
        
#if email==True:
if email:#Forma simplificada. En el if, si no pones nada, supones que la variable es ==True.
    print("Email es correcto")
else:
    print("Email no es correcto")
    
    
    