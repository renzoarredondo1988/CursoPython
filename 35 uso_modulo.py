#En este archivo usaremos un modulo guardado en la carpeta "Paquetes" el archivo calculos_generales

#Para llamar al archivo, se usa from Nombre_del_Paquete.nombre_Modulo import funcion_modulo
#El asterisco llama a todas las funciones del modulo
#from Paquetes_Video35.calculos_generales  import * #Este ejemplo es para un paquete

#se pueden generar subpaquetes dentro del paquete principal, para modularizar aun mas, y tener mejor orden
#cada uno debera tener el archivo con extension py __init__
#Llamaremos a dichos modulos dentro de esos subpaquetes con el metodo del punto

from Paquetes_Video35.basicos.operaciones_basicas import *
from Paquetes_Video35.redondeo_potencia.redondea_y_potencia import *

dividir(4,6)