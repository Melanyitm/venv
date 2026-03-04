from pydantic import BaseModel 

class Persona(BaseModel):
    nombre : str
    apellido : str
    edad : int 

Juan = Persona(nombre = "Juan", apellido = "Morales", edad = 30)

from pydantic import ValidationError

try:
    Persona(nombre = "Juan", apellido = "Morales", age = 30 )
except ValidationError as ex:
    print(ex)