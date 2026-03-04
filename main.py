from fastapi import FastAPI
from pydantic import BaseModel

class Persona(BaseModel):
    nombre : str
    apellido : str
    edad : int

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/personal")
def crear(usuario : Persona):
    print(usuario)
    return True