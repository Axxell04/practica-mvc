from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from views import app_router

app = FastAPI()
app.mount("/src", StaticFiles(directory="./src"), "src")
app.include_router(app_router)