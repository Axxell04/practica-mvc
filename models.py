import sqlite3
from pydantic import BaseModel

class Miembro(BaseModel):
    id_miembro: int
    nombre: str

class Tarea(BaseModel):
    id_tarea: int
    id_miembro: int
    descripcion: str


db = sqlite3.connect("db.db")

with db:
    cursor = db.cursor()
    
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS miembros 
                (
                    id_m INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(20)
                )
                """)
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS tareas 
                (
                    id_t INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_m INTEGER ,
                    descripcion TEXT,
                    FOREIGN KEY (id_m) REFERENCES miembros(id_m)
                )
                """)
    
def listar_miembros():
    with db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM miembros")
        res = cursor.fetchall()
        lista = []
        for reg in res:
            lista.append(Miembro(id_miembro=reg[0], nombre=reg[1]))
        return lista

def agregar_miembro(nombre: str):
    with db:
        cursor = db.cursor()
        cursor.execute("INSERT INTO miembros (nombre) VALUES (?)", (nombre,))
        
def eliminar_miembro(id):
    with db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM miembros WHERE id_m = ?", (id,))
        cursor.execute("DELETE FROM tareas WHERE id_m = ?", (id,))

def listar_tareas(id_miembro: int):
    with db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM tareas WHERE id_m = ?", (id_miembro,))
        res = cursor.fetchall()
        lista = []
        for reg in res:
            lista.append(Tarea(id_tarea=reg[0], id_miembro=reg[1], descripcion=reg[2]))
        return lista
            
def agregar_tarea(id_miembro: int, descripcion: str):
    with db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM miembros WHERE id_m = ?", (id_miembro,))
        if len(cursor.fetchall()) > 0:
            cursor.execute("INSERT INTO tareas (id_m, descripcion) VALUES (?,?)", (id_miembro, descripcion))
        else:
            print("ID miembro no encontrada")                

def eliminar_tarea(id_tarea: int):
    with db:
        cursor = db.cursor()
        cursor.execute("DELETE FROM tareas WHERE id_t = ?", (id_tarea,))
        
        
# agregar_miembro("Yandry")
# listar_miembros()
# eliminar_miembro(1)
# print(listar_miembros())
# agregar_tarea(2, "Desarrollar Backend")
# listar_tareas(2)
# eliminar_miembro(1)
# eliminar_tarea(2)
# listar_tareas(2)

        
    