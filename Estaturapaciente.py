#importacion de las librerias
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit, texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final=f"{limpio[:2]}-{limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0, tk.END)
        fechaN.insert(0, formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.strptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
#Lista de pacientes(inicialmente vacía)
paciente_data=[]
 
def guardar_en_archivo():
    with open("paciente.txt","w",encoding="utf-8") as archivo:
        for paciente in paciente_data:
            archivo.write(f"{paciente['Nombre']}|{paciente['Fecha de Nacimiento']}|{paciente['Edad']}|"
                          f"{paciente['Genero']}|{paciente['Grupo Sanguíneo']}|"
                          f"{paciente['Tipo de Seguro']}|{paciente['Centro Médico']}|{paciente['Estatura del Paciente']}\n")
                         
           
#Función para registrar paciente
def registrarPaciente():
#Crear un diccionario con los datos ingresados
    paciente={
        "Nombre":nombreP.get(),
        "Fecha de Nacimiento":fechaN.get(),
        "Edad":edadVar.get(),
        "Genero":genero.get(),
        "Grupo Sanguíneo":entryGrupoSanguineo.get(),
        "Tipo de Seguro":tipo_seguro.get(),
        "Centro Médico":centro_medico.get(),
        "Estatura del Paciente": estaturaP.get()
    }
    #Agregar paciente a la lista
    paciente_data.append(paciente)
    #Linea modificada 07/09/2025
    guardar_en_archivo()
    #Recargar el Treeview
    cargar_treeview()
 
#Cargar el treeview
    cargar_treeview()
def cargar_treeview():
    #Limpiar el treeview
    for paciente in treeview.get_children():
        treeview.delete(paciente)
    #Insertar cada paciente
    for i, item in enumerate(paciente_data):
        treeview.insert(
            "","end",iid=str(i),
            values=(
                item["Nombre"],
                item["Fecha de Nacimiento"],
                item["Edad"],
                item["Genero"],
                item["Grupo Sanguíneo"],
                item["Tipo de Seguro"],
                item["Centro Médico"],
                item["Estatura del Paciente"]        
            )
        )        
def cargar_desde_archivo_pacientes():
    try:
        with open ("pacienteEstatura.txt", "r", encoding="utf-8") as archivo:
         paciente_data.clear()
         for linea in archivo:
             datos=linea.strip().split("|")
             if len (datos)==7:
                paciente={
                    "Nombre":datos[0],
                    "Fecha de Nacimiento": datos[1],
                    "Edad": datos[2],
                    "Genero": datos[3],
                    "Grupo Sanguíneo":datos[4],
                    "Tipo de Seguro": datos[5],
                   "Centro Médico": datos[6],
                   "Estatura del Paciente": datos[7]      
                }
                paciente_data.append(paciente)
        cargar_treeview()
    except FileNotFoundError:
        open("pacienteEstatura.text", "w", encoding="utf-8").close()
def eliminar_paciente():
    seleccionado=treeview.selection()
    if seleccionado:
        indice=int(seleccionado[0])
        id_item=seleccionado[0]
        if messagebox.askyesno("Eliminar Paciente",f"¿ Esta seguro de eliminar el paciente '{treeview.item(id_item,'values')[0]}'?"):
            del paciente_data[indice]
            guardar_en_archivo() #Guardar los cambios en le archivo
            cargar_treeview()
            messagebox.showinfo("Eliminar Paciente","Paciente eliminado exitosamente.")
        else: #este else es del if selecionado
            messagebox.showwarning("Eliminar Paciente", "No se a seleccionado ningun paciente.")
            return
#crear ventana principal
ventana_principal= tk.Tk()
ventana_principal.title("Libro de Pacientes")
ventana_principal.geometry("400x600")
#Crear contenedor Notebook (pestañas)
pestañas=ttk.Notebook(ventana_principal)
#Crear frames(uno por pestaña)
frame_pacientes=ttk.Frame(pestañas)
#Agregar pestañas al Notebook
pestañas.add(frame_pacientes, text="Pacientes")
#Mostrar las pestañas en la ventana
pestañas.pack(expand=True, fill="both")
#Nombre
labelNombre=tk.Label(frame_pacientes, text="Nombre Completo: ")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", pady=5, padx=5)
#Fecha de nacimiento
labelFechaN=tk.Label(frame_pacientes, text="Fecha de Nacimiento:")
labelFechaN.grid(row=1, column=0, sticky="w", pady=5, padx=5)
validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes, validate="key", validatecommand=(validacion_fecha, '%P')) #llamado a la función de enmascarar fecha
fechaN.grid(row=1, column=1, sticky="w", pady=5, padx=5)
#Edad
labelEdad=tk.Label(frame_pacientes, text="Edad: ")
labelEdad.grid(row=2, column=0, sticky="w", pady=5, padx=5)
edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, sticky="w", pady=5, padx=5)
#Genero
labelGenero=tk.Label(frame_pacientes, text="Genero: ")
labelGenero.grid(row=3, column=0, sticky="w", pady=5, padx=5,)
#radiobutton
genero=tk. StringVar()
genero.set("Masculino") #Valor por defecto
radioMasculino=ttk.Radiobutton(frame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5, pady=5)
radioFemenino=ttk.Radiobutton(frame_pacientes, text="Femenino", variable=genero, value="Femenino")
radioFemenino.grid(row=4, column=1, sticky="w", padx=5, pady=5)
#Grupo Sanguineo
labelGrupoSanguineo=tk.Label(frame_pacientes, text=" Grupo Sanguineo: ")
labelGrupoSanguineo.grid(row=5, column=0, sticky="w", padx=5, pady=5)
entryGrupoSanguineo=tk.Entry(frame_pacientes)
entryGrupoSanguineo.grid(row=5, column=1, sticky="w", padx=5, pady=5)
#Tipo de Seguro
labelTipoSeguro=tk.Label(frame_pacientes, text="Tipo de Seguro: ")
labelTipoSeguro.grid(row=6, column=0, sticky="w", padx=5, pady=5)
tipo_seguro=tk.StringVar()
tipo_seguro.set("Publico")#Valor por defecto
comboTipoSeguro=ttk.Combobox(frame_pacientes, values=["Público", "Privado","Ninguno"], textvariable=tipo_seguro)
comboTipoSeguro.grid(row=6, column=1, sticky="w", padx=5, pady=5)
#Centro Medico
labelCentroMedico=tk.Label(frame_pacientes, text="Centro de Salud: ")
labelCentroMedico.grid(row=7, column=0, sticky="w", padx=5, pady=5)
centro_medico=tk.StringVar()
centro_medico.set("Hospital Central") #Valor por defecto
comboCentroMedico=ttk.Combobox(frame_pacientes, values=["Hospital Central", "Clinica Norte", "Centro Sur"], textvariable=centro_medico)
comboCentroMedico.grid(row=7, column=1, sticky="w", padx=5, pady=5)
#Estatura deL paciente
labelEstatura=tk.Label(frame_pacientes, text="Estatura del Paciente: ")
labelEstatura.grid(row=8, column=0, sticky="w", padx=5, pady=5)
estaturaP=tk.StringVar()
estaturaP=tk.Entry(frame_pacientes)
estaturaP.grid(row=8, column=1, sticky="w", pady=5, padx=5)
# Frame para los Botones,registar o eliminar, TREEVIEW
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky="w")
#Boton Registrar
btn_registrar=tk.Button(btn_frame, text="Registrar", command=registrarPaciente, bg="#008000")
btn_registrar.grid(row=0, column=0, padx=5, pady=5)
#Boton Eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command=eliminar_paciente, bg="#FF0000")
btn_eliminar.grid(row=0, column=1,padx=5, pady=5)
#crear treeview para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes, columns=("Nombre", "FechaN","Edad", "Genero", "GrupoS", "TipoS", "CentroM", "EstaturaP"), show="headings")
#Definir Encabezados
treeview.heading("Nombre", text="Nombre Completo")
treeview.heading("FechaN", text="Fecha Nacimiento")
treeview.heading("Edad", text="Edad")
treeview.heading("Genero", text="Genero")
treeview.heading("GrupoS", text="Grupo Sanguineo")
treeview.heading("TipoS", text="Tipo Seguro")
treeview.heading("CentroM", text="Centro Medico")
treeview.heading("EstaturaP", text="Estatura del Paciente")
#definir anchos de columnas
treeview.column("Nombre", width=120)
treeview.column("FechaN", width=120)
treeview.column("Edad", width=50, anchor="center")
treeview.column("Genero", width=60, anchor="center")
treeview.column("GrupoS", width=100, anchor="center")
treeview.column("TipoS", width=100, anchor="center")
treeview.column("CentroM", width=120, anchor="center")
treeview.column("EstaturaP", width=120, anchor="center")
#Ubicar el treeview en la cuadrícula
treeview.grid(row=10, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
#Scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes, orient="vertical", command=treeview.yview)
scroll_y.grid(row=10, column=2, sticky="ns")
 
cargar_desde_archivo_pacientes()#cargar dttos desde el archivo al iniciar la aplicacion
 
ventana_principal.mainloop()