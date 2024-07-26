import pickle

#Creamos una clase para generar objetos del tipo Personal que tendra un constructor con los datos del argumento
class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha generado una persona con el nombre de ",self.nombre)

    def __str__(self):#Este metodo convierte en string todo lo que se ingrese
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

#La idea es guardar en un fichero externo las personas con su informacion, eso lo haremos en listas
#para eso, creamos una clase ListaPersonas, con la variable personas que sera una lista vacia
class ListaPersonas:
    personas=[]

    #Creamos un constructor de modo tal que cada vez que se invoque al mismo, se cree un fichero con los codigos
    #binarios de los objetos que se agreguen de la clase persona
    def __init__(self):
        listaDePersonas=open("ficheroExterno","ab+")#Crea un fichero con nombre ficheroExterno, el ab+ indica
        #que puedo, desde py, agregar info binaria
        listaDePersonas.seek(0)#Cada vez que agrego un objeto, pongo el cursor al principio

       #Con el bloque try except eliminamos la posibilidad de que arroje error la primera vez cuando el fichero este vacio
        try:
            self.personas = pickle.load(listaDePersonas)  # llamamos a la lista personas=[] y cargamos listaDePersonas en binario en
           # el fichero
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self,p):
        self.personas.append(p)
        self.guardarPersonasFicheroExterno()#una vez que se agrego la persona, llama al metodo que lo guarda
        #en el fichero externo

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasFicheroExterno(self):
        listaDePersonas=open("ficheroExterno","wb")#Recordar que es el metodo para guardar cosas en el fichero
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente: ")
        for p in self.personas:
            print(p)


miLista=ListaPersonas() #Objeto del tipo ListaPersonas. Al crear este objeto, podemos utilizar sus metodos
p=Persona("Julia","Femenino",99)#Objeto del tipo persona
miLista.agregarPersonas(p) #Agregamos el objeto del tipo Persona al objeto ListasPersonas


miLista.mostrarPersonas()
miLista.mostrarInfoFicheroExterno()
