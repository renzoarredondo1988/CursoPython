
#Programa que evalua si hay un arroba o no en un correo
email=input("Introduce tu email, por favor: ")

for i in email:
    if i=="@":
        arroba=True
        
        break;
        
else: #Vemos que el else no pertenece al if (identacion), sino al bucle for. Si al recorrer todo el bucle,
    #no se encontro con ningun arroba, el mismo sera falso. Caso contrario, sera verdadero.
    arroba=False
    
print(arroba)