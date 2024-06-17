import tkinter as tk
from paciente.vista import Frame, barra_menu

def main():
    ventana = tk.Tk()
    ventana.title('Administración de Pacientes')
    icono = tk.PhotoImage(file="img/icon.png")
    ventana.iconphoto(True, icono)
    ventana.resizable(0,0)

    barra_menu(ventana)
    app = Frame(root = ventana)
    

    ventana.mainloop()

if __name__ == '__main__':
    main()