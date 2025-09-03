# Importación de librerías
import tkinter as tk
from tkinter import ttk, messagebox
 
# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("500x600")
 
# Crear contenedor Notebook (pestañas)
pestañas = ttk.Notebook(ventana_principal)
 
# Crear frames para cada pestaña
frame_pacientes = ttk.Frame(pestañas)
frame_doctores = ttk.Frame(pestañas)
 
# Agregar pestañas
pestañas.add(frame_doctores, text="Doctores")
pestañas.pack(expand=True, fill="both")
 
#Pestaña Doctores
# Título
tituloDoctores = tk.Label(frame_doctores, text="Registro de Doctores", font=("Arial", 14, "bold"))
tituloDoctores.grid(row=0, column=0, columnspan=2, pady=10)
 
# Nombre
labelNombreD = tk.Label(frame_doctores, text="Nombre:")
labelNombreD.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entryNombreD = tk.Entry(frame_doctores, width=30)
entryNombreD.grid(row=1, column=1, padx=10, pady=5)
 
# Especialidad (Combobox)
labelEspecialidad = tk.Label(frame_doctores, text="Especialidad:")
labelEspecialidad.grid(row=2, column=0, sticky="e", padx=10, pady=5)
especialidad = tk.StringVar()
comboEspecialidad = ttk.Combobox(frame_doctores, textvariable=especialidad, state="readonly",
values=["Cardiología", "Neurología", "Dermatología"], width=28)
comboEspecialidad.grid(row=2, column=1, padx=10, pady=5)
comboEspecialidad.set("Cardiología")
 
# Edad 
labelEdad = tk.Label(frame_doctores, text="Edad:")
labelEdad.grid(row=3, column=0, sticky="e", padx=10, pady=5)
spinEdad = tk.Spinbox(frame_doctores, from_=0, to=100, width=5, justify="center")
spinEdad.grid(row=3, column=1, sticky="w", padx=10, pady=5)
 
# Teléfono
labelTelefono = tk.Label(frame_doctores, text="Teléfono:")
labelTelefono.grid(row=4, column=0, sticky="e", padx=10, pady=5)
entryTelefono = tk.Entry(frame_doctores, width=30)
entryTelefono.grid(row=4, column=1, padx=10, pady=5)
 
# Funciones
def registrar_doctor():
    nombre = entryNombreD.get()
    espec = comboEspecialidad.get()
    edad = spinEdad.get()
    telefono = entryTelefono.get()
 
    if not nombre or not espec or not edad or not telefono:
        messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos.")
        return
 
    treeview.insert("", "end", values=(nombre, espec, edad, telefono))
    entryNombreD.delete(0, tk.END)
    comboEspecialidad.set("Cardiología")
    spinEdad.delete(0, tk.END)
    spinEdad.insert(0, "25")
    entryTelefono.delete(0, tk.END)
 
def eliminar_doctor():
    seleccion = treeview.selection()
    if not seleccion:
        messagebox.showinfo("Eliminar", "Selecciona un doctor para eliminar.")
        return
    for item in seleccion:
        treeview.delete(item)
 
# Botones
btn_frameD = tk.Frame(frame_doctores)
btn_frameD.grid(row=5, column=0, columnspan=2, pady=10)
 
btn_registrarD = tk.Button(btn_frameD, text="Registrar", bg="green", fg="white", width=15, command=registrar_doctor)
btn_registrarD.grid(row=0, column=0, padx=10)
 
btn_eliminarD = tk.Button(btn_frameD, text="Eliminar", bg="red", fg="white", width=15, command=eliminar_doctor)
btn_eliminarD.grid(row=0, column=1, padx=10)
 
# Tabla Treeview
treeview = ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad", "Edad", "Telefono"), show="headings")
treeview.heading("Nombre", text="Nombre")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Teléfono")
 
treeview.column("Nombre", width=120)
treeview.column("Especialidad", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Telefono", width=100)
treeview.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
scroll_yD = ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
scroll_yD.grid(row=6, column=2, sticky="ns")
treeview.configure(yscrollcommand=scroll_yD.set)
 
ventana_principal.mainloop()
 