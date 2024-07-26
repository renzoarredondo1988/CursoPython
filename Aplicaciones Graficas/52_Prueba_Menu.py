from tkinter import *
from tkinter import messagebox #Resulta que para usar ventanas emergentes hay q importarlas aparte

root=Tk()


#Segun el metodo que usemos, sera la estructura de la ventana, por ej, showwarning muestra un simbolo de exclamacion
def infoAdicional():
    messagebox.showinfo("Procesadormde Renzo","Procesador de texto 2024")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia")

def salirAplicacion():
    #valor=messagebox.askquestion("Salir","Deseas salir de la aplicacion?")
    #el metodo .askquestion devuelve un no o un yes segun que boton pulsemos

    valor = messagebox.askokcancel("Salir", "Deseas salir de la aplicacion?")
#El metodo askokcancel devuelven un True or False
    if valor==True:
        root.destroy()

def cerrarDocumento():
    messagebox.askretrycancel("Reintentar","No es posible cerrar documento bloqueado")


barraMenu=Menu(root)
root.config(menu=barraMenu, width=300,height=300)

archivoMenu=Menu(barraMenu,tearoff=0)#el tearoff saca un interlinedo que arroja x defecto py
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()#Crea una barra de separacion
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)

archivoEdicion=Menu(barraMenu,tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu)

archivoAyuda=Menu(barraMenu,tearoff=0)
archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)#El label indica el texto que llevara el menu, el
#menu pregunta que objeto contiene el label

barraMenu.add_cascade(label="Edicion",menu=archivoEdicion)

barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)

barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)


root.mainloop()