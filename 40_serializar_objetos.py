import pickle

class Vehiculos():#Clase vehiculo, clase padre o superclase
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enMarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enMarcha=True

    def acelera(self):
        self.acelera=True

    def frena(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enMarcha,
              "\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)


coche1=Vehiculos("Mazda","MKZ")

coche2=Vehiculos("Fiat","Uno")

coche3=Vehiculos("Chevrolet","Corsa")

coches=[coche1,coche2,coche3]

fichero=open("losCoches","wb")#Escritura de byte "wb" es el permiso con el q vamos a escribir este fichero

pickle.dump(coches,fichero)

fichero.close()
del (fichero)

ficheroApertura=open("losCoches","rb")

misCoches=pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estado())

