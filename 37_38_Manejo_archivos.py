from io import open

archivo_texto=open("archivo.txt","w") #Crea un archivo .txt, la w significa q es un archivo de escritura "write"

frase="Estupendo dia para estudiar Phyton \n Martes"

archivo_texto.write(frase) #Metodo de la clase io, agrega el texto frase a archivo_texto

archivo_texto.close() #Siempre que se crea un archivo y se manipula, hay q cerrarlo
#Este cierre es en la memoria desde el programa Py, no en Windows

archivo_texto=open("archivo.txt","r")#archivo que ya existe en modo lectura "read"

texto=archivo_texto.read() #Metodo que lee lo que hay dentro de un archivo y lo almacena en la variable texto

archivo_texto.close()

print(texto)

archivo_texto=open("archivo.txt","r")

lineas_texto=archivo_texto.readlines()#Devuelve las lineas en una lista

archivo_texto.close()

print(lineas_texto)

print(lineas_texto[0]) #Solo imprime el primer renglon ya que es una lista, se almacena en indice 0

archivo_texto=open("archivo.txt","a")#a de appends, agrega lineas de texto

archivo_texto.write("\n Siempre es una buena opcion estudiar py")

archivo_texto.close()

archivo_texto=open("archivo.txt","r")

print(archivo_texto.read())#Cuando lee el archivo, lo hace de inicio a fin, quedando el cursor en el final

print(archivo_texto.read()) #Por lo cual, si repetimos la instruccion no pasara nada, porque el cursor quedo
#en el final...

archivo_texto.seek(22)#Esta instruccion mueve al cursor al numero de caracter que deseemos, siendo el 0 el primero

print(archivo_texto.read())

archivo_texto.seek(0)#llevo el puntero al inicio neuvamente

print(archivo_texto.read(11))#el read funciona al reves, te dice hasta que caracter queres q lea

archivo_texto.seek(len(archivo_texto.read())/2)#Situo el cursor en la mitad. Recordar que el len indica cant caracteres

print(archivo_texto.read())

archivo_texto.close()

archivo_texto=open("archivo.txt","r+")#Permite leer y escribir el archivo

archivo_texto.write("Comienzo del texto \n ")#Esto me agrega los valores al inicio, ya q cada vez q abre el archivo
#para escribir lo hace en la posicion inicial

print(archivo_texto.readlines())

archivo_texto.seek(0)

lista_texto=archivo_texto.readlines();

print(lista_texto)

lista_texto[1]="Esta linea de texto ha sido incluida desde el exterior \n"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()


