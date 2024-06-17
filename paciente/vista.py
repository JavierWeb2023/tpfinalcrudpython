import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from estructura.consultas import Pacientes, listar_especialidad, listar_medicos, listar_pacientes, guardar_paciente, editar_paciente, borrar_paciente

def barra_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_archivo = tk.Menu(barra, tearoff=0)
    menu_consultar = tk.Menu(barra, tearoff=0)
    menu_ayuda = tk.Menu(barra, tearoff=0)


    #principal

    barra.add_cascade(label='Archivo', menu = menu_archivo)
    barra.add_cascade(label='Consultar', menu = menu_consultar)
    barra.add_cascade(label='Ayuda', menu = menu_ayuda)

    #submenuarchivo
    menu_archivo.add_command(label='Conectar DB')
    menu_archivo.add_command(label='Desconectar DB')
    menu_archivo.add_command(label='Salir', command= root.destroy)

    #submenuconsultar
    menu_consultar.add_command(label='Consulta 1')
    menu_consultar.add_command(label='Consulta 2')
    menu_consultar.add_command(label='Consulta 3')
    menu_consultar.add_command(label='Consulta 4')

    #submenuayuda
    menu_ayuda.add_command(label='Acerca de ...')


class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480,height=320)
        self.root = root
        self.pack()
        self.id_paciente = None
        self.label_form()
        self.input_form()
        self.botones_principales()
        self.mostrar_tabla()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial',14,'bold','italic'))
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)

        self.label_apellido = tk.Label(self, text="Apellido: ")
        self.label_apellido.config(font=('Arial',14,'bold','italic'))
        self.label_apellido.grid(row= 0, column=1,padx=10,pady=10)

        self.label_historia = tk.Label(self, text="Historia Nº: ")
        self.label_historia.config(font=('Arial',14,'bold','italic'))
        self.label_historia.grid(row= 2, column=0,padx=10,pady=10)

        self.label_telefono = tk.Label(self, text="Teléfono: ")
        self.label_telefono.config(font=('Arial',14,'bold','italic'))
        self.label_telefono.grid(row= 2, column=1,padx=10,pady=10)

        self.label_especialidad = tk.Label(self, text="Especialidad: ")
        self.label_especialidad.config(font=('Arial',14,'bold','italic'))
        self.label_especialidad.grid(row= 0, column=2,padx=10,pady=10)
    
    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre)
        self.entry_nombre.config(width=25, bg='#FFFFFF', state='disabled',font=('Arial',12,'italic'))
        self.entry_nombre.grid(row= 1, column=0,padx=10,pady=10, columnspan='1')

        self.apellido = tk.StringVar()
        self.entry_apellido = tk.Entry(self,textvariable=self.apellido)
        self.entry_apellido.config(width=25, bg='#FFFFFF', state='disabled',font=('Arial',12,'italic'))
        self.entry_apellido.grid(row= 1, column=1,padx=10,pady=10, columnspan='1')

        self.historia = tk.StringVar()
        self.entry_historia = tk.Entry(self,textvariable=self.historia)
        self.entry_historia.config(width=25, bg='#FFFFFF', state='disabled',font=('Arial',12,'italic'))
        self.entry_historia.grid(row= 3, column=0,padx=10,pady=10, columnspan='1')

        self.telefono = tk.StringVar()
        self.entry_telefono = tk.Entry(self,textvariable=self.telefono)
        self.entry_telefono.config(width=25, bg='#FFFFFF', state='disabled',font=('Arial',12,'italic'))
        self.entry_telefono.grid(row= 3, column=1,padx=10,pady=10, columnspan='1')


        x = listar_especialidad()
        y = []
        for i in x:
            y.append(i[1])

        self.especialidad = ['Seleccione uno'] + y
        self.entry_especialidad = ttk.Combobox(self, state="readonly")
        self.entry_especialidad['values'] = self.especialidad
        self.entry_especialidad.current(0)
        self.entry_especialidad.config(width=25, state='disabled',font=('Arial',12,'italic'))
        self.entry_especialidad.bind("<<ComboboxSelected>>")
        self.entry_especialidad.grid(row= 1, column=2,padx=10,pady=10, columnspan='1')

    def botones_principales(self):
        self.btn_nuevo = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_nuevo.config(width= 20,font=('Arial', 12,'bold','italic'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_nuevo.grid(row= 5, column=0,padx=10,pady=10)

        self.btn_guardar = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_guardar.config(width= 20,font=('Arial', 12,'bold','italic'),fg ='#FFFFFF' , bg='#0000FF',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_guardar.grid(row= 5, column=1,padx=10,pady=10)

        self.btn_cancelar = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cancelar.config(width= 20,font=('Arial', 12,'bold','italic'),fg ='#FFFFFF' , bg='#FF0000',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cancelar.grid(row= 5, column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_historia.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_especialidad.config(state='normal')
        self.btn_guardar.config(state='normal')
        self.btn_cancelar.config(state='normal')
        self.btn_nuevo.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_historia.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_especialidad.config(state='disabled')
        self.entry_especialidad.current(0)
        self.btn_guardar.config(state='disabled')
        self.btn_cancelar.config(state='disabled')
        self.nombre.set('')
        self.apellido.set('')
        self.historia.set('')
        self.telefono.set('')
        self.id_paciente = None
        self.btn_nuevo.config(state='normal')
    
    def guardar_campos(self):
        paciente = Pacientes(
            self.nombre.get(),
            self.apellido.get(),
            self.historia.get(),
            self.telefono.get(),
            self.entry_especialidad.current()
        )

        if self.id_paciente == None:
            guardar_paciente(paciente)
        else:
            editar_paciente(paciente, int(self.id_paciente))

        self.mostrar_tabla()
        self.bloquear_campos()
    
    def mostrar_tabla(self):
        self.lista_p = listar_pacientes()
        self.lista_p.reverse()
        self.tabla = ttk.Treeview(self, columns=('Nombre','Apellido','Historia','Telefono','Especialidad'))
        self.tabla.grid(row=6,column=0,columnspan=6,padx=10,pady=0,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=5,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='Historia')
        self.tabla.heading('#4',text='Telefono')
        self.tabla.heading('#5',text='Especialidad')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values = (p[1],p[2],p[3],p[4],p[7]))
        
        self.btn_modificar = tk.Button(self, text='Modificar',command=self.editar_registro)
        self.btn_modificar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_modificar.grid(row=7,column=0,padx=10,pady=10)

        self.btn_eliminar = tk.Button(self, text='Eliminar', command=self.eliminar_registro)
        self.btn_eliminar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#FF0000',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_eliminar.grid(row=7,column=1,padx=10,pady=10)


        self.label_medicos = tk.Label(self, text="Médicos:")
        self.label_medicos.config(font=('Arial',14,'bold','italic'))
        self.label_medicos.grid(row=8,column=0,padx=10,pady=10)

        self.lista_m = listar_medicos()
        self.lista_m.reverse()
        self.tabla2 = ttk.Treeview(self, columns=('Nombre','Apellido','Especialidad'))
        self.tabla2.grid(row=8,column=1,columnspan=4,padx=10,pady=10,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla2.yview)
        self.scroll.grid(row=8, column=4,padx=0,pady=10,sticky='nse')
        self.tabla2.configure(yscrollcommand= self.scroll.set)

        self.tabla2.heading('#0',text='ID')
        self.tabla2.heading('#1',text='Nombre')
        self.tabla2.heading('#2',text='Apellido')
        self.tabla2.heading('#3',text='Especialidad')

        for m in self.lista_m:
            self.tabla2.insert('',0,text=m[0],
                              values = (m[1],m[2],m[5]))
    

    def editar_registro(self):
        try:
            self.id_paciente = self.tabla.item(self.tabla.selection())['text']

            self.nombre_paciente_m = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_paciente_m = self.tabla.item(self.tabla.selection())['values'][1]
            self.historia_paciente_m = self.tabla.item(self.tabla.selection())['values'][2]
            self.telefono_paciente_m = self.tabla.item(self.tabla.selection())['values'][3]
            self.especialidad_paciente_m = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre.set(self.nombre_paciente_m)
            self.apellido.set(self.apellido_paciente_m)
            self.historia.set(self.historia_paciente_m)
            self.telefono.set(self.telefono_paciente_m)
            self.entry_especialidad.current(self.especialidad.index(self.especialidad_paciente_m))

        except:
            pass
    

    def eliminar_registro(self):
        confirmar = messagebox.askyesno(message="Confirma la eliminación del paciente?", title="Eliminar paciente")

        if confirmar == True:
            self.id_paciente = self.tabla.item(self.tabla.selection())['text']
            borrar_paciente(int(self.id_paciente))
            self.mostrar_tabla()
            self.id_paciente = None
        else:
            pass