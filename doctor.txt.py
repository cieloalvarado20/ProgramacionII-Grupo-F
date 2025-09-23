#importacion de las librerias
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
#
doctor_data=[]
#para guardar datos
def guardar_en_archivo():
    with open("doctor.txt","w",encoding="utf-8") as archivo:
        for doctor in doctor_data:
            archivo.write(f"{doctor['Nombre']}|{doctor['Especialidad']}|{doctor['Años de Experiencia']}|"
                          f"{doctor['Genero']}|{doctor['Hospital']}\n")
           
#Función para registrar doctor
def registrarDoctor():
#Crear un diccionario con los datos ingresados
    doctor={
        "Nombre":nombreP.get(),
        "Especialidad":especialidad.get(),
        "Años de Experiencia":spin.get(),
        "Genero":genero.get(),
        "Hospital":hospital.get()
    }
#Agregar paciente a la lista
    doctor_data.append(doctor)
#linea modificada
    guardar_en_archivo()
#Cargar el treeview
    cargar_treeview()
def cargar_treeview():
    #Limpiar el treeview
    for doctor in treeview.get_children():
        treeview.delete(doctor)
    #Insertar cada paciente
    for i, item in enumerate(doctor_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Especialidad"],
                item["Años de Experiencia"],
                item["Genero"],
                item["Hospital"]        
            )
        )        
       
#
def cargar_desde_archivo_doctores():
    try:
        with open ("doctor.txt", "r", encoding="utf-8") as archivo:
         doctor_data.clear()
         for linea in archivo:
             datos=linea.strip().split("|")
             if len (datos)==7:
                doctor={
                    "Nombre":datos[0],
                    "Especialidad": datos[1],
                    "Años de Experiencia": datos[2],
                    "Genero": datos[3],
                    "Hospital":datos[4],    
                }
                doctor_data.append(doctor)
        cargar_treeview()
    except FileNotFoundError:
        open("doctor.txt", "w", encoding="utf-8").close()
#crear ventana principal
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
#Nombre
labelNombre=tk.Label(frame_doctores, text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreP=tk.Entry(frame_doctores)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
#Especialidad
labelEspecialidad=tk.Label(frame_doctores, text="Especialidad: ")
labelEspecialidad.grid(row=1, column=0, sticky="w", padx=5, pady=5)
especialidad=tk.StringVar()
especialidad.set("Neurologia")#Valor por defecto
comboEspecialidad=ttk.Combobox(frame_doctores, values=["Neurologia", "Cardiologia","Ginecologia","Traumatologia"], textvariable=especialidad)
comboEspecialidad.grid(row=1, column=1, sticky="w", padx=5, pady=5)
#años de experiencia
labelAñosExperiencia=tk.Label(frame_doctores, text="Años de Experiencia")
labelAñosExperiencia.grid(row=2,column=0, padx=5, pady=5, sticky="w")
spin=tk.Spinbox(frame_doctores, from_=1, to=100)
spin.grid(row=2,column=1, padx=5, pady=5, sticky="w")
#Genero
labelGenero=tk.Label(frame_doctores, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5,)
#radiobutton
genero=tk. StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_doctores, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5, pady=5)
radioFemenino=ttk.Radiobutton(frame_doctores, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5, pady=5)
#Hospital
labelHospital=tk.Label(frame_doctores, text="Hospital: ")
labelHospital.grid(row=5, column=0, sticky="w", padx=5, pady=5)
hospital=tk.StringVar()
hospital.set("Hospital")#Valor por defecto
comboHospital=ttk.Combobox(frame_doctores, values=["Hospital Central", "Hospital Norte ","Clinica Vida","Clinica Santa Maria"], textvariable=hospital)
comboHospital.grid(row=5, column=1, sticky="w", padx=5, pady=5)
# Frame para los Botones,registar o eliminar, TREEVIEW
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky="w")
#Boton Registrar
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarDoctor)
btn_registrar.grid(row=0, column=0, padx=5, pady=5)
btn_registrar.configure(bg="#008000")
#crear treeview para mostrar pacientes
treeview=ttk.Treeview(frame_doctores, columns=("Nombre", "Especialidad","Años de Experiencia", "Genero", "Hospital"), show="headings")
#Definir Encabezados
treeview.heading("Nombre", text="Nombre")
treeview.heading("Especialidad", text="Especialidad")
treeview.heading("Años de Experiencia", text="Año de Experiencia")
treeview.heading("Genero", text="Genero")
treeview.heading("Hospital", text="Hospital")
#definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("Especialidad", width=120)
treeview.column("Años de Experiencia", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("Hospital", width=100, anchor="center")
#Ubicar el treeview en la cuadrícula
treeview.grid(row=7, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_doctores, orient="vertical", command=treeview.yview)
scroll_y.grid(row=7, column=2, sticky="ns")
 
 
 
cargar_desde_archivo_doctores()#cargar datos desde el archivo all iniciar la aplicacion
ventana_principal.mainloop()
 