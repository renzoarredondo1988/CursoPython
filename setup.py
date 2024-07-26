#Video 36
#los paquetes que nosotros hagamos son distribuibles a cualquer maquina. Para ello, lo que debemos hacer
#es "instalar" ese paquete en la pc donde querramos trabajar, de modo que sea accecible a los modulos que
#contiene el mismo

from setuptools import setup #Primera instruccion para generar un paquete distribuible

setup(#En los argumentos de la funcion se pondran todos los datos de configuracion

    name="paquetecalculos",
    version=1.0,
    description="Paquete de redondeo",
    author="Renzo",
    author_email="renzo.mau1988@gmail.com",
    packages=["Paquetes_Video35","Paquetes_Video35.redondeo_potencia"]#se pone nombre del paquete, nombre del subpaquete desde la ruta


)

#Una vez dada estas caracteristicas, lo que se hace es abrir la consola en donde se creo el archivo setup y se
#pone la instruccion python setup.py sdist
#Veremos que se habran creado dos carpetas. una se llama dist, tendra los archivos del paquete distribuible que hemos creado
#Ese es el archivo que debemos compartir por la plataforma que querramos para que otros tengan nuestro paquete distribuible