from fastapi.responses import FileResponse
import models

def get_index():
    return FileResponse("./src/index.html")

def get_miembros():
    return models.listar_miembros()

def add_miembro(nombre: str):
    return models.agregar_miembro(nombre)

def remove_miembro(id_miembro: int):
    return models.eliminar_miembro(id_miembro)

def get_tareas(id_miembro: int):
    return models.listar_tareas(id_miembro)

def add_tarea(id_miembro: int, descripcion: str):
    return models.agregar_tarea(id_miembro, descripcion)

def remove_tarea(id_tarea: int):
    return models.eliminar_tarea(id_tarea)