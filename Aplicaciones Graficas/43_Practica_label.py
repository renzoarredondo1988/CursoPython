from tkinter import *

#Creamos una raiz y un frame como vimos en la clase anterior
root=Tk()

miFrame=Frame(root,width=738,height=1599)

miFrame.pack()

#milabel=Label(miFrame,text="Hola alumnos de Python")#La clase label permite insertar texto, imagenes, etc.
#ya sea a una raiz, a un frame o a un widget, pero que estaran estaticas (no interactuan)
#milabel.place(x=100,y=200)#Si empaquetamos con .pack, la ventana se adapta al tamaño del Label.
#Con el metodo .place lo que hacemos es determinar en que punto del frame queremos el texto

#Si solo se va a usar una sola variable Label, se puede reducir el codigo de la siguiente manera:
#Label(miFrame,text="Hola alumnos de Python",fg="red",font=("Comic Sans MS",18)).place(x=100,y=200)

miImagen=PhotoImage(file="foto_perfil.png")

Label(miFrame,image=miImagen).place(x=0,y=0)

root.mainloop()

