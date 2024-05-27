from fastapi import APIRouter
from pydantic import BaseModel
import controller

class Request(BaseModel):
    nombre: str = ""
    descripcion: str = ""
    id_miembro: int = 0
    id_tarea: int = 0    

app_router = APIRouter()

@app_router.get("/")
async def inicio():
    return controller.get_index()

@app_router.get("/get_miembros")
async def get_miembros():
    return controller.get_miembros()

@app_router.post("/add_miembro")
async def add_miembro(request: Request):
    return controller.add_miembro(request.nombre)

@app_router.delete("/remove_miembro")
async def remove_miembro(request: Request):
    return controller.remove_miembro(request.id_miembro)

@app_router.get("/get_tareas/{id_miembro}")
async def get_tareas(id_miembro: int):
    return controller.get_tareas(id_miembro)

@app_router.post("/add_tarea")
async def add_tarea(request: Request):
    return controller.add_tarea(request.id_miembro, request.descripcion)

@app_router.delete("/remove_tarea")
async def remove_tarea(request: Request):
    return controller.remove_tarea(request.id_tarea)