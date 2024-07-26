#La funcion map aplica una funcion a una lista iterable


numeros=[17,24,7,39,8,51,92]

print(list(filter(lambda numero_par:numero_par%2==0,numeros)))

class Empleado():

    def __init__(self,nombre,cargo,salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {}$".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[

    Empleado("Juan", "Director", 6700),

    Empleado("Ana", "Presidenta", 7500),

    Empleado("Antonio", "Administrativo", 2100),

    Empleado("Daniel", "Administrativo", 2150),

    Empleado("Mario", "Botones", 1800)

]

def calculo_comision(empleado):

    if empleado.salario<=3000:
        empleado.salario=empleado.salario*1.03
        return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)