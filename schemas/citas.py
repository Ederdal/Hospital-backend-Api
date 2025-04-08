"""Esquemas Pydantic para la entidad Cita."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from models.citas import MyEstatusCita


class CitaBase(BaseModel):
    """Campos base para una cita médica."""

    Persona_ID: int
    Hora_Cita: datetime
    Telefono: str
    Correo_Electronico: str
    Motivo_Cita: str
    Estatus: MyEstatusCita


class CitaCreate(CitaBase):
    """Esquema para la creación de una cita médica."""


class CitaUpdate(BaseModel):
    """Esquema para la actualización parcial de una cita médica."""

    Persona_ID: Optional[int] = None
    Hora_Cita: Optional[datetime] = None
    Telefono: Optional[str] = None
    Correo_Electronico: Optional[str] = None
    Motivo_Cita: Optional[str] = None
    Estatus: Optional[MyEstatusCita] = None
    Fecha_Actualizacion: Optional[datetime] = None


class CitaResponse(CitaBase):
    """Esquema de respuesta para una cita médica."""

    ID: int
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True
