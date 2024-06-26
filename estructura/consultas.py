from .conexiondb import ConeccionDB

def crear_tabla():
    conn = ConeccionDB()

    sql = '''
            CREATE TABLE IF NOT EXISTS Especialidad(
            idEspecialidad INTEGER NOT NULL, 
            Nombre VARCHAR(100),
            PRIMARY KEY (idEspecialidad AUTOINCREMENT)
            );

            CREATE TABLE IF NOT EXISTS Medicos(
            idMedico INTEGER NOT NULL, 
            Nombre VARCHAR(100),
            PRIMARY KEY (idMedico AUTOINCREMENT)
            );

            CREATE TABLE IF NOT EXISTS Pacientes(
            idPaciente INTEGER NOT NULL, 
            Nombre VARCHAR(60),
            Apellido VARCHAR(60),
            Historia VARCHAR(60),
            Telefono VARCHAR(60),
            Especialidad INTEGER,
            Medico INTEGER,
            PRIMARY KEY (idPaciente AUTOINCREMENT),
            FOREIGN KEY (Especialidad) References Especialidad(idEspecialidad),
            FOREIGN KEY (Medico) References Medicos(idMedico)
            );
            '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()

    except:
        pass

def listar_especialidad():
    conn = ConeccionDB()
    listar_especialidad = []
    sql = """
            SELECT * FROM Especialidad
         """
    
    try:
        conn.cursor.execute(sql)
        listar_especialidad = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_especialidad
    except:
        pass

def listar_pacientes():
    conn = ConeccionDB()
    listar_pacientes = []
    sql = """
            SELECT *
            FROM Pacientes as P
            inner join Especialidad as E
            on P.Especialidad = E.idEspecialidad
            inner join Medicos as M
            on P.Medico = M.idMedico
         """
    
    try:
        conn.cursor.execute(sql)
        listar_pacientes = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_pacientes
    except:
        pass

def listar_medico():
    conn = ConeccionDB()
    listar_medico = []
    sql = """
            SELECT * FROM Medicos
         """
    
    try:
        conn.cursor.execute(sql)
        listar_medico = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_medico
    except:
        pass


class Pacientes:
    def __init__(self, nombre, apellido, historia, telefono, especialidad, medico):
        self.id_pacientes = None
        self.nombre = nombre
        self.apellido = apellido
        self.historia = historia
        self.telefono = telefono
        self.especialidad = especialidad
        self.medico = medico

    def __str__(self):
        return f'Paciente[{self.nombre},{self.apellido},{self.historia},{self.telefono},{self.especialidad},{self.medico}]'


def guardar_paciente(paciente):
    conn = ConeccionDB()

    sql = f"""
            INSERT INTO Pacientes (Nombre,Apellido,Historia,Telefono,Especialidad,Medico)
            VALUES('{paciente.nombre}','{paciente.apellido}','{paciente.historia}','{paciente.telefono}',{paciente.especialidad},{paciente.medico});
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()


def editar_paciente(paciente, id):
    conn = ConeccionDB()

    sql = f"""
            UPDATE Pacientes
            SET Nombre = '{paciente.nombre}', Apellido = '{paciente.apellido}', Historia = '{paciente.historia}', Telefono = '{paciente.telefono}', Especialidad = {paciente.especialidad}, Medico = {paciente.medico}
            WHERE idPaciente = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()


def borrar_paciente(id):
    conn = ConeccionDB()

    sql = f"""
            DELETE FROM Pacientes WHERE idPaciente = {id};
            """
    
    conn.cursor.execute(sql)
    conn.cerrar_con()