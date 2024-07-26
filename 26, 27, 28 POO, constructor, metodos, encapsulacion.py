#Video 26 - POO, creacion de clase, creacion de metodo
# 27 - Creacion de constructor, encapsulamiento de variable o atributo
# 28 - Encapsulamiento de metodos

class Coche(): #Creo la clase coche

#Un constructor es un metodo especial que da caracteristicas y comportamientos iniciales a un objeto
    def __init__(self): #Constructor, sintaxis en Python
         self.__largoChasis=2500 #se utiliza el self.atributo para dar un estado inicial al constructor
         self.__anchoChasis=1200 #esto es asi porque sino el atributo se genera como una variable local dentro
         self.__ruedas=4 #del metodo, y no como un atributo del constructor, por lo que no podriamos acceder a el
         self.__enMarcha=False  #La clase coche tiene 4 estados o propiedades

 #Poner un __atributo, lo que nos permite es encapsular el atributo, es decir, que no se pueda modificar "manualmente"
#Desde el exterior de la clase, pero si sera accesible desde dentro de la propia clase. Cuando llamemos a las variables
#Encapsuladas desde metodos, debemos hacerlo con los dos guiones bajos

#Los metodos definen el comportamiento de un objeto
#Por eje, un coche puede arrancar, parar, etc
#Un metodo es una funcion especial que pertenece a una clase que se este creando, mientras que una funcion no
#pertenece a ninguna clase
    def arrancar(self,arrancamos):#Sintaxis de un metodo. def nombre_del_metodo(argunmento):
        self.__enMarcha=arrancamos #self hace referencia al propio objeto perteneciente a la clase
        #El self, en otros lenguajes es equivalente al this (Ej.Java). En JAVA por ejemplo esta implicito dentro
        #del argumento, en phyton, estamos obligados a ponerlo
        #Cuando nostros accedemos al metodo arrancar, el self esta haciendo referencia al objeto u objetos instanciados.
        #En este caso, solo hemos creado un objeto llamado miCoche, es decir, que el metodo esta recibiendo como
        #parametro en lugar de self, miCoche, y luego seria miCoche.__enMarcha=arrancamos. Pero en lugar del objeto
        #la sintaxis es self. En otros lenguajes esto es "transparente", no se coloca nada, y se interpreta solo
        #Py si nos obliga
        #Vemos que el metodo arrancar va a recibir otro parametro "arrancamos", segun si le pasamos que es
        #True o false va a ser la condicion, en funcion de eso ingresara al condicional para saber si esta
        #en marcha o parado
        if(self.__enMarcha):
            chequeo=self.__chequeo_interno() #Creamos un metodo para definir si estaba todo bien en el auto cdo arranca
            #Video 28. ese metodo devuelve un booleano, q lo guardaremos en la variable local chequeo
            #si esa condicion esta ok, nos devuelve que el coche esta en marcha

        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"

        elif (self.__enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche esta parado"


#Generamos el metodo chequeo interno, que verifica el estado del combustible, aceite y puertas. Obviamente
#Que para poder verificarlo, el auto minimamente deberia estar en "contacto", aunque en nuestro ejercicio
#hablaremos de que el coche esta encendido o arrancado. Por lo cual, no se deberia poder acceder a este metodo
#En cualquier momento, sino solo despues de que el coche esta en marcha. Para ello, es necesario encapsular el
#metodo, para ello le agregamos dos guiones bajo. Al encapsularlo, al igual que los atributos, solo podremos
#acceder al metodo desde la propia clase, es decir dentro del metodo arrancar. Se encapsulara metodos o atributos
#segun la logica del programa y del programador.
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

    #El comportamiento estado solo nos dara informacion del estado del objeto Coche
    def estado(self): #La clase coche tiene 2 comportamientos, arrancar o estado. Esto son metodos. Le dan accion a nuestro objeto
        print("El coche tiene ",self.__ruedas," ruedas. Un ancoh de ",self.__anchoChasis," y un largo de ",
              self.__largoChasis)


miCoche=Coche()     #Instanciar una clase o instancia objeto o ejemplificar una clase. Es decir, al objeto coche le damos las caracteristicas de la clase coche

#print("El largo del coche es ",miCoche.largoChasis) #Accedemos a una propiedad del coche
#print("La cantidad de ruedas del coche son ",miCoche.ruedas)

print(miCoche.arrancar(True))#El metodo arrancar requiere que le digamos el parametro "arrancar"

miCoche.estado()

print("----------A continuacion creamos el segundo objeto----------")


miCoche2=Coche() #Genero mi segundo objeto que comparte clase con el primero

#print("El largo del coche es ",miCoche2.largoChasis) #Accedemos a una propiedad del coche
#print("La cantidad de ruedas del coche son ",miCoche2.ruedas)


print(miCoche2.arrancar(False))
#miCoche2.ruedas=5 #Vemos que si no hay encapsulacion se puede modificar desde fuera de la clase
miCoche2.__ruedas=5
miCoche2.estado()


