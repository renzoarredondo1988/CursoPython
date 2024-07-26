from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir",initialdir="/",filetypes=(("Ficheros de excel","*.xlsx"),
    ("Archivos de texto","*.txt")))

    print(fichero)

Button(root,text="Abrir fichero",command=abreFichero).pack()

root.mainloop()