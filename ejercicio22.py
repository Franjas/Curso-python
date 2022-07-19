#Crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter as tk

#Ventana del programa:
window = tk.Tk()  # variable window

window.title('Aplicación')
window.geometry('205x290')
window.resizable(width=False, height=False)
window.config(bg='green4')

#Label
titulo = tk.Label(window,
    text='Deportes favoritos',
    font='consolas 12 bold',
    bg='darkorchid4',
    fg='turquoise3',
    relief=tk.RAISED,
    border=5)
titulo.pack(fill= tk.X, pady=5)


##CheckBotones:
cuadro = tk.LabelFrame(window,
    bg='wheat',
    text='Especialidades',
    font='arial 11 underline')


op1 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Futbol',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op1)
checkbox.grid()


op2 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Béisbol',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op2)
checkbox.grid()


op3 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Natación',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op3)
checkbox.grid()


op4 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Tenis',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op4)
checkbox.grid()


op5 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Baloncesto',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op5)
checkbox.grid()


op6 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Voleibol',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op6)
checkbox.grid()


op7 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Bádminton',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op7)
checkbox.grid()


op8 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Hockey',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op8)
checkbox.grid()


op9 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Formula 1',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op9)
checkbox.grid()


op10 = tk.StringVar()
checkbox = tk.Checkbutton(cuadro,
                          text='Moto GP',
                          bg='wheat',
                          font='consola 8 bold',
                          width=10, anchor=tk.W,
                          variable=op10)
checkbox.grid()

cuadro.pack()


##Botón siguiente:
sig = tk.Button(window,
    text='Siguiente',
    font=('arial', 10),
    bg='blue2', fg='white',
    relief='groove', bd=3)
sig.pack(pady=5)

window.mainloop()