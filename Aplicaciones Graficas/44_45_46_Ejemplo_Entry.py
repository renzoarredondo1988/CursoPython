from tkinter import *

#En esta clase lo que vemos es que para agregar frames y no se nos empiece a superponer unos con otro, o tener
#problemas con las ubicaciones de los diferentes gadgets, frames y labels, lo que hacemos es usar
#el metodo .grid, que lo que hace es "dividir" el frame en diferentes casillas, de modo tal que tengamos
#nuestro frame dividido en posiciones y trabajar por ubicaciones
raiz=Tk()

miFrame=Frame(width=600,height=600)
miFrame.pack()

miNombre=StringVar()#le esta diciendo a la variable miNombre que recibira una variable String al pulsar el boton
#Los entrys son cuadros en donde podemos escribir texto
cuadroNombre=Entry(miFrame,textvariable=miNombre)#Le esta diciendo al cuadroNombre que se complete con la variable miNombre que se acciona al pulsar el boton enviar, que a su vez llama a la funcion que setea la variable
cuadroNombre.grid(row=0,column=1,padx="5",pady="5")#Le indico a mi entrada cuadroTexto en la fila 0 columna 1 del grid o cuadro
cuadroNombre.config(fg="red",justify="center")

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=3,column=1,padx="5",pady="5")
cuadroPassword.config(show="*")#Con la propiedad show decimos q solo muestre asteriscos

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx="5",pady="5")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2,column=1,padx="5",pady="5")

textoComentario=Text(miFrame,width=16,height=5)#Cuando colocamos miFrame dentro de las clases, estamos diciendo que el contenedor
#padre de ese label, gadget o lo que sea esta siendo contenido por miFrame.
textoComentario.grid(row=4,column=1,padx="5",pady="5") #Con la clase Text agregamos un cuadro para agregar texto

scrollVert=Scrollbar(miFrame,command=textoComentario.yview)#con esta clase lo q hacemos es agregar la barrita
#de scroll, con el primer argumento lo que hacemos es indicar en donde esta contenido, con el segundo le estamos
#indicando que ese scroll pertenece al objeto textoComentario, con el metodo y.view le estamos diciendo que sera
#una barra de scroll en el eje y
scrollVert.grid(row=4,column=2,sticky="nsew")#el sticky en este caso hace q el scroll sea del tamaño del espacio del texto

textoComentario.config(yscrollcommand=scrollVert.set)#Con este metodo hacemos que el scroll se ubique en la
#posicion en la que esta el texto

nombreLabel=Label(miFrame,text="Nombre ")
nombreLabel.grid(row=0,column=0,sticky="e",padx="5",pady="5")#Pongo el label nombre en la posicion 0, entonces me queda a la misa altura
#que cuadro texto, pero una posicion antes en el eje de las x, entonces me aseguro que nunca se superpongan

apellidoLabel=Label(miFrame,text="Apellido ")
apellidoLabel.grid(row=1,column=0,sticky="e",padx="5",pady="5")#La opcion sticky nos permite correr para un lado u otro el texto
#segun puntos cardinales (e,s,n,w)

direccionLabel=Label(miFrame,text="Direccion ")
direccionLabel.grid(row=2,column=0,sticky="e",padx="5",pady="5")#El pad es un marco que permite tomar distancias
#en x y en y de cada label, frame, etc, ademas se le puede dar propiedades

passwordLabel=Label(miFrame,text="Contraseña ")
passwordLabel.grid(row=3,column=0,sticky="e",padx="5",pady="5")

comentariosLabel=Label(miFrame,text="Comentarios ")
comentariosLabel.grid(row=4,column=0,sticky="e",padx="5",pady="5")

def codigoBoton():
    miNombre.set("Juan")#La funcion set establece un valor a una variable

botonEnvio=Button(raiz,text="enviar",command=codigoBoton) #con el command le estamos diciendo q al pulsar
#el boton, el codigo vaya a la funcion codigoBoton
botonEnvio.pack()

raiz.mainloop()

#En google, poniendo entry tkinter py podemos ver los diferentes opciones q son banda
#si buscas Text python tmb