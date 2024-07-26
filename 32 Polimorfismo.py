#El polimorfismo en POO es una propiedad en el que el objeto cambia de forma segun el entorno en el
#que se encuentre
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

#El polimorfismo me permite crear un metodo cuyo argumento sea un objeto. Al recibir ese objeto como parametro
#llamamos al metodo desplazamiento que es comun en las 3 clases creadas. Como ese llamado depende del objeto
#que se uso como parametro, el programa sabra a cual metodo de cual clase esta llamando
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()


miVehiculo=Camion()
desplazamientoVehiculo(miVehiculo)

miVehiculo2=Coche()
desplazamientoVehiculo(miVehiculo2)