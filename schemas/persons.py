"""Esquemas Pydantic para la entidad Persona."""

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime, date
from uuid import UUID


class PersonBase(BaseModel):
    Titulo_Cortesia: str = Field(..., example="Dr.")
    Nombre: str = Field(..., example="Carlos")
    Primer_Apellido: str = Field(..., example="Ramírez")
    Segundo_Apellido: str = Field(..., example="Gómez")
    CURP: str = Field(..., example="RAGC890101HDFLNN09")
    Correo_Electronico: str = Field(..., example="carlos.ramirez@example.com")
    Telefono: str = Field(..., example="5551234567")
    Fecha_Nacimiento: date = Field(..., example="1989-01-01")
    Fotografia: Optional[str] = Field(None, example="https://example.com/photo.jpg")
    Genero: str = Field(..., example="Masculino")
    Tipo_Sangre: str = Field(..., example="O+")
    Estatus: bool = Field(..., example=True)
    Fecha_Registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    pass


class Person(PersonBase):
    ID: UUID = Field(..., example="3fa85f64-5717-4562-b3fc-2c963f66afa6")

    class Config:
        from_attributes = True
