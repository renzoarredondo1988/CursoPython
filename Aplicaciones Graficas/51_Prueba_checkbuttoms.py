from tkinter import *

root=Tk()
root.title("Ejemplo")

foto=PhotoImage(file="foto_practica.png")
Label(root,image=foto).pack()#Recordatorio, el primer argumento corresponde a donde va a pertenecer el Label
#el segundo, le estamos diciendo que el label va a contener la foto que trajimos antes, y luego, empaquetamos

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""

    if playa.get()==1:
        opcionEscogida+="Playa"

    if montagna.get()==1:
        opcionEscogida+="Montaña"

    if turismoRural.get()==1:
        opcionEscogida+="Turismo Rural"

    textoFinal.config(text=opcionEscogida)

frame=Frame(root)
frame.pack()

Label(frame,text="Elige destinos",width=50).pack()

Checkbutton(frame,text="Playa",variable=playa,onvalue=1,offvalue=0,command=opcionesViaje).pack()#onvalue lo que hace es verifica si el tilde esta activado o no
#si esta activado, en este caso devuelve un 1, y si no, el offvalue devuelve un 0

Checkbutton(frame,text="Montaña",variable=montagna,onvalue=1,offvalue=0,command=opcionesViaje).pack()

Checkbutton(frame,text="Turismo rural",variable=turismoRural,onvalue=1,offvalue=0,command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()