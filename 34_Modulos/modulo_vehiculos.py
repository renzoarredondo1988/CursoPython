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


#Clase hija Furgoneta
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"




#Clase hija Moto  comparte atributos y metodos de la clase Vehiculo, y tendra los propios de la clase
class Moto(Vehiculos):
    hcaballito="" #asi le llaman los gallegos a los wheellies, generamos un atributo que no dice nada
    def caballito(self):#hacemos un metodo que al acceder a el indica que hacemos caballito
        self.hcaballito="Voy haciendo caballito"
#Vemos que el atriubto hcaballito no esta dentro del metodo estado, lo cual es logico, porque no todos
#los vehiculos pueden hacer caballito. Seria un error escribir la variable self.hcaballito en vehiculo por este motivo

#La solucion es sobreescribir el metodo agregando el atributo o metodo que deseamos ver

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn Marcha: ",self.enMarcha,
              "\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,"\nCaballido: ",self.hcaballito)

#Creamos una clase que no hereda de ninguna otra para vehiculos electricos (Video 30)
#En video 31 hacemos que VElectricos herede de Vehiculos, llame al constructor de la superclase con el super()
#y le agregamos que el constructor de VElectricos nos pida una marca y modelo que meteremos en el constructor padre
class VElectricos(Vehiculos):
    def __init__(self,marca,modelo):

        super().__init__(marca,modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True

#Creamos una clase que tendra herencia multiple. Por que? Porque una bicicleta electrica compartiria todos
#los atributos y metodos que contiene la clase Vehiculos, pero ademas los que tiene la clase VElectricos
#En la herencia multiple, la clase que pongamos primera en el parametro que hereda es la que tendra mayor
#peso respecto a su constructor. Es decir, que en este caso, al poner primero VElectricos, el constructor
#Que hereda es de esa clase, cuyo constructor no requiere de parametros.
#En los casos que se compartan metodos con el mismo nombre en las clases padres, el metodo que
# se sobrepondra sera el de la clase que se encuentre mas a la izquierda. En el caso de los constructores
#es el metodo __init__
class BicicletaElectrica(VElectricos,Vehiculos):
    pass

