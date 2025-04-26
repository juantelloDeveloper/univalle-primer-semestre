'''
Autor: sebastian
Fecha:22-4-2025
'''


from tkinter import *
import os
ventana = Tk()

# Diccionario de datos
colors = {
    # Llave : # Valor
    "negro": "#000000",
    "blanco": "#ffffff"
}

def principal():
    nombre = ctNombre.get()

    varSalida.set("Hola " + nombre)
    
ventana.title("Formulario")

# tkinter para poder saber donde se encuentra el bitmap para poner el icono
# necesita el path relativo, por lo cual usamos la librera os del sistema.
ventana.iconbitmap(os.path.join(os.path.dirname(__file__), "myicon.ico"))

# Se define el tamaño de la vantana donde w(ancho) x h(alto)
ventana.geometry("400x400")
# 1 = True, 0 = False
puede_cambiar_tamaño_del_ancho = True
puede_cambiar_tamaño_del_alto = False

ventana.resizable(puede_cambiar_tamaño_del_ancho,puede_cambiar_tamaño_del_alto)
ventana.config(bg=colors["blanco"])


contenedor1 = Frame(ventana)
contenedor1.config(width=250, height=100, bd = 5, relief="sunken")
eNombre = Label(contenedor1, text="Name: ")
eNombre.grid(row=0, column=0, padx=3 , pady=3)
ctNombre = Entry(contenedor1,width= 15)
ctNombre.grid(row=0, column=1, padx=3, pady=3)
bNombre = Button(contenedor1,text= "Saludar ", command= principal)
bNombre.grid(row=1, columnspan=2, padx=3, pady=3)
contenedor1.pack(pady=10)


contenedor2 = LabelFrame(ventana, text="salida")
contenedor2.config(width=150, height=75, bd = 5, relief="sunken")
varSalida = StringVar()
ctSalida = Entry(contenedor2, width=20, textvariable= varSalida,state="readonly")
ctSalida.grid(row=1, columnspan=2, padx=3, pady=3)
contenedor2.pack(pady=5)


ventana.mainloop()
