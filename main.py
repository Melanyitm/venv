from datetime import date, time
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


# Lista donde se guardan las reservas 
reservas: list["Reserva"] = []


# Modelo de datos con Pydantic
class Reserva(BaseModel):
    """Modelo de salas."""

    id_reserva: Optional[str] = None
    id_sala: str = Field(..., min_length=1, description="Identificador de la sala")
    id_usuario: str = Field(..., min_length=1, description="Identificador del usuario")
    fecha: date = Field(..., description="Fecha de la reserva")
    hora_inicio: time = Field(..., description="Hora de inicio")
    hora_fin: time = Field(..., description="Hora de fin")
    personas: int = Field(..., ge=1, description="Número de asistentes")
    estado: str = Field(..., min_length=1, description="Estado de la reserva")


# Crear la instancia de la aplicación web
app = FastAPI(title="Sistema de Reservas de Salas", version="1.0.0")



@app.get("/")
def read_root():
    return {"message": "Sistema de Reservas de Salas - API"}


@app.post("/reservas", response_model=Reserva)
def registrar_reserva(reserva: Reserva) -> Reserva:
    """Registra una nueva reserva de sala."""

    if reserva.id_reserva is None:
        reserva.id_reserva = f"RES-{len(reservas) + 1:04d}"

    reservas.append(reserva)

    return reserva

@app.get("/reservas", response_model=list[Reserva])
def consultar_reservas() -> list[Reserva]:
    """Consulta todas las reservas registradas."""
    return reservas