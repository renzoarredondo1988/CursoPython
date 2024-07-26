#Cuando llamamos a un modulo, Py siempre busca que este en el mismo directorio (carpeta) en la que se encuentra
#el archivo que esta llamando al modulo. Si no lo encuentra, lo buscara en el syspath (carpeta en donde
# se encuentra instalado python). Si movemos al modulo de carpeta, arrojara error.
#Lo aconsejable es que los archivos se guarden paquetes, basicamente son carpetas que contienen archivos
#py con modulos relacionados entre si. De esta forma nos permite organizar.



from modulo_vehiculos import *

miCoche=Vehiculos("Renault","Kangoo")
miCoche.estado()