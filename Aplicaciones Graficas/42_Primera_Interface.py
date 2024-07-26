from tkinter import *

#Vamos a usar la libreria tkinder para aplicaciones graficas. Hay otras.
#Por lo tanto, importamos clase y metodos de la misma para crear ventana, frame y widgets
#Una interfaz grafica tiene una raiz o ventana que funciona a modo de contenedor general,
#frame que agrupa diferentes widgets (botones, barras, menues, etc)

raiz=Tk()#usando la clase Tk creamos la ventana

raiz.title("Ventana de pruebas")#Metodo para agregar un titulo a nuestra ventana

#raiz.resizable(0,0)#Este metodo nos imposibilita de modificar el tamaño de una ventana. Pide como parametros
#El alto y ancho, cuanto se puede modificar

raiz.iconbitmap("foto.ico")#Este metodo permite agregar una imagen a la ventanita de la izq. Tiene q ser si o si extension .ico

#raiz.geometry("650x350")#Metodo para determinar alto y ancho

raiz.config(bg="blue")#Configuramos el color del fondo

miFrame=Frame()#Llamamos a la clase Frame para crear un frame (o agrupador de widgets). Crearlo por si solo, no lo
#vincula a la ventana que hemos creado

miFrame.pack(side="bottom",anchor="w") #Metodo para "empaquetar" o meter el frame en la raiz o ventana

miFrame.config(bg="green")

miFrame.config(width="300",height="300")



raiz.mainloop()#Este metodo siempre debe estar al final

#Para que al abrir el archivo no nos abra la consola detras, hay que cambiar la extension del archivo .py
#por .pyw

