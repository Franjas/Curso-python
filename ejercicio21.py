#Crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.

from tkinter import *


def selec():
    monitor.config(text="Opción {}".format(opcion.get()))

def reset():
    opcion.set(None)          # Reiniciamos el seleccionable
    monitor.config(text='')   # Reiniciamos la etiqueta

ventana = Tk()
ventana.config(bd=15)
ventana.config(bg='lightblue')

opcion = IntVar()

Radiobutton(ventana, text="Opción 1", variable=opcion,
            value=1, command=selec).pack()
Radiobutton(ventana, text="Opción 2", variable=opcion,
            value=2, command=selec).pack()
Radiobutton(ventana, text="Opción 3", variable=opcion,
            value=3, command=selec).pack()

monitor = Label(ventana)
monitor.pack()
Button(ventana, text="Reiniciar", command=reset).pack()
ventana.mainloop()