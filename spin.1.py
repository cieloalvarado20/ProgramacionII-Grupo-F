import tkinter as tk
from tkinter import messagebox
def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionadaes: {spin.get()}")
def mostrarGenero():
    tk.messagebox.showinfo("Genero", f"El genero seleccionado es:{genero.get()}")
ventana=tk.Tk()
#Spinbox de numeros del 1 al 10
labelEdad=tk.Label(ventana, text="Edad")
labelEdad.grid(row=0,column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(ventana, from_=1, to=10)
spin.grid(row=0,column=1, padx=10, pady=10)
boton=tk.Button(ventana, text="Obtener Valor",command=mostrarEdad)
boton.grid(row=1, column=0, padx=10, pady=10)
#Genero
labelGenero=tk.Label(ventana,text="Genero")
labelGenero.grid(row=2, column=0, padx=5, pady=5, sticky="w")
"#Spinbox de texto para genero"
genero=tk.Spinbox(ventana, values=("Masculino","Femenino","Otro"))
genero.grid(row=2, column=1, padx=10, pady=10)
botonGenero=tk.Button(ventana, text="Obtener genero", command= mostrarGenero)
botonGenero.grid(row=3, column=0, padx=10, pady=10)
ventana.mainloop()
 