#importacion de las librerias
import tkinter as tk
from tkinter import ttk, messagebox
#lista de pacientes(iniciativa vacia)
doctores_data=[]
#funcion registrar paciente
def registrarDoctor():
    #crear un diccionario con los datos ingresados
    doctor={
        "Nombre": nombreP.get(),
        "Especialidad": especialidad.get(),
        "Edad": spin.get(),
        "Telefono": entryTelefono.get(),
    }
    #agregar paciente a la lista
    doctores_data.append(doctor)
    #cargar el treewiew
    cargar_treeview()
def cargar_treeview():
    #Limpiar el treeview
    for doctor in treeview.get_children():
        treeview.delete(doctor)
        #insertar cada paciente
    for i, item in enumerate(doctores_data):
        treeview.insert(
            "","end", iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Edad"],
                item["Telefono"],
                )
        )
ventana_principal= tk.Tk()
ventana_principal.title("Libro de Pacientes y Doctores")
ventana_principal.geometry("400x600")
#Crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al Notebook
pestañas.add(frame_pacientes, text="Pacientes")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
#pestaña doctores
frame_doctores=ttk.Frame(pestañas)
pestañas.add(frame_doctores, text="Doctores")
pestañas.pack(expand= True, fill="both")
# Título
tituloDoctores = tk.Label(frame_doctores, text="Registro de Doctores", font=("Arial", 14, "bold"))
tituloDoctores.grid(row=0, column=0, columnspan=2, pady=10)
#Nombre
labelNombre=tk.Label(frame_doctores, text="Nombre Completo: ")
labelNombre.grid(row=1, column=0, sticky="w", padx=5, pady=5)
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Especialidad
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad: ")
labelEspecialidad.grid(row=7, column=0, sticky="w", padx=5, pady=5)
especialidad=tk.StringVar()
especialidad.set("Neurologia")#Valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Neurologia", "Cardiologia","Ginecologia"], textvariable=especialidad)
comboEspecialidad.grid(row=7, column=1, sticky="w", padx=5, pady=5)
#Edad
labelEdad=tk.Label(frame_doctores, text="Edad")
labelEdad.grid(row=8,column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(frame_doctores, from_=1, to=100)
spin.grid(row=8,column=1, padx=5, pady=5, sticky="w")
#Telefono
labelTelefono=tk.Label(frame_doctores, text="Telefono: ")
labelTelefono.grid(row=9, column=0, sticky="w", padx=5, pady=5)
entryTelefono=tk.Entry(frame_doctores)
entryTelefono.grid(row=9, column=1, sticky="w", padx=5, pady=5)
# Frame para los Botones,       registar o eliminar, TREEVIEW
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky="w")
#Boton Registrar
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarDoctor)
btn_registrar.grid(row=0, column=4, padx=5, pady=5)
btn_registrar.configure(bg="#008000")
#Boton Eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=5,padx=5, pady=5)
btn_eliminar.configure(bg="#FF0000")
#crear treeview para mostrar pacientes
treeview=ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad","Edad", "Telefono"), show="headings")
#Definir Encabezados
treeview.heading("Nombre", text="Nombre")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Edad", text="Edad")
treeview.heading("Telefono", text="Telefono")
#definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("Especialidad", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Telefono", width=60, anchor="center")
#Ubicacín de treeview en la columna
treeview.grid(row=11, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
scroll_y.grid(row=11, column=2, sticky="ns")
 
ventana_principal.mainloop()