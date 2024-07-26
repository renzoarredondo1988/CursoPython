class Persona(): #Creamos una clase persona
    def __init__(self,nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia

    def descripcion(self):
        print("Nombre ",self.nombre," Edad ",self.edad," Lugar de residencia ",self.lugar_residencia)

#Creamos una clase empleado
#El diseño de herencia siempre usa el principio de sustitucion. En español decimos "Es siempre un"
#Ej. un Empleado es siempre una persona. Pero una persona no siempre es un empleado. Eso nos permite
#Definir bien si estamos aplicando bien la herencia o no.
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):

       # super().__init__("Antonio",55,"España")#Con este metodo y sintaxis, llamamos a la clase padre
       #si lo dejo asi, todos los empleados se llamaran Antonio, tendran 55 años y seran de españa.

        super().__init__(nombre_empleado,edad_empleado,residencia_empleado)#De esta forma, para llamar al constructor
       #de empleado, me pide parametros que luego ingresaran al metodo super, llenando los datos individualmente
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
         super().descripcion()
         print("Salario: ",self.salario," Antiguedad: ",self.antiguedad)

#Al crear un objeto del tipo persona, debemos pasar los parametros con el nombre, edad y lugar de residencia
#Ahora si esa persona es a su vez un empleado, y lo creamos instanciando a la clase Empleado, ya no podremos
#pasar los parametros nombrados, ya que el constructor de la clase Empleado nos pide salario y antiguedad, no
#los atributos de nombre, edad y lugar.
Manuel=Empleado(1500,15,"Manuel",55,"España") #Podriamos crear el objeto Antonio de la clase Empleado, pero no acceder al metodo
#Descripcion, porque daria error por faltarnos los datos de nombre, edad y antiguedad. Para eso, dentro de
#la clase Empleado, usamos el metodo super, que lo que hace es llamar al constructor de la clase padre

Manuel.descripcion() #Para que en la descripcion figuren el salario y la antiguedad, hay que sobreescribir
#el metodo descripcion, creado en la clase Persona. En lugar de copiar y pegar todo el metodo, lo que hacemos
#es usar super().nombre_metodo. De esa forma estamos llamando al metodo de la clase padre, y podemos agregar
#los nuevos valores que querramos mostrar

print(isinstance(Manuel,Empleado))#isinstance es un metodo que nos devuelve un Booleano
print(isinstance(Manuel,Persona))#basicamente nos indica si un objeto pertenece o hereda de una clase o no
#basandonos en la propiedad de la herencia "es siempre un/a"