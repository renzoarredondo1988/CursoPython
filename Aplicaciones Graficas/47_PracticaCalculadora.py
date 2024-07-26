from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

operacion=""

resultado=0

numeroPantalla=StringVar() #Creamos una variable numeroPantalla, con la clase StringVar lo que haciamos
#Es crear una variable del tipo cadena que asociaremos a los widgets correspondientes

#---------------------pantalla-----------------------------------
pantalla=Entry(miFrame,textvariable=numeroPantalla)#asociamos numeroPantalla al Entry pantalla

pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)#con el columnspan lo que le estamos diciendo al grid
#es que la pantalla ocupara 4 columnas de ancho (diseño web)
pantalla.config(background="black",fg="#03f943",justify="right")

#----------------- pulsaciones Teclado ---------------------

def numeroPulsado(num):

    global operacion

    if operacion!="":#Aca estamos diciendo que si hay algun valor diferente a vacio, significa que el usuario ha
        #pulsado algun valor de operacion, por lo tanto, en la pantalla solo se tendra que setear el numero nuevo ingresado
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)#Aca le estamos diciendo a la funcion que lo que va a escribir en pantalla
    #va a ser lo que haya (numeroPantalla.get(), y a eso se le sumara el 4

#-------------- funcion suma ---------------------------------------

def suma(num):
    global operacion #con la palabra reservada global, lo que hacemos es que se modifique la variable "operacion"
    #creada fuera de la funcion
    global resultado
    resultado+=int(num) #Todos los valores que se ingresan por un cuadro de texto son del tipo Str, por eso hay q convertirlos a int
    operacion="suma"
    numeroPantalla.set(resultado)

#-------------------- funcion igual el_resultado -------------------------
def el_resultado():
    global resultado
    numeroPantalla.set(resultado+int(numeroPantalla.get()))
    resultado=0


#------------------------fila1-----------------------------
boton7=Button(miFrame,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/",width=3)
botonDiv.grid(row=2,column=4)

#------------------------fila2-----------------------------
#Respeco a lambda:numeroPulsado("4"). Py lee el programa de arriba a abajo, si nosotros en numeroPulsado pasamos
#El parametro 4, el programa lo toma como un llamado a la funcion numeroPulsado, aun sin haber apretado el boton
#Con las funciones lambda se soluciona ese problema
boton4=Button(miFrame,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="X",width=3)
botonMult.grid(row=3,column=4)

#------------------------fila3-----------------------------
boton1=Button(miFrame,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonResta=Button(miFrame,text="-",width=3)
botonResta.grid(row=4,column=4)

#------------------------fila4-----------------------------
boton0=Button(miFrame,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",",width=3,command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=",width=3, command=lambda:el_resultado())
botonIgual.grid(row=5,column=3)
botonSuma=Button(miFrame,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=5,column=4)


raiz.mainloop()