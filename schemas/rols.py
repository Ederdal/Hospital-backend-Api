"""Esquemas Pydantic para la entidad Rol."""

from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID


class RolBase(BaseModel):
    Nombre: str = Field(..., example="Administrador")
    Descripcion: Optional[str] = Field(None, example="Acceso completo a todos los módulos del sistema")
    Estatus: bool = Field(..., example=True)
    Fecha_Registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")
    Fecha_Actualizacion: Optional[datetime] = Field(None, example="2025-04-01T10:00:00.000Z")


class RolCreate(RolBase):
    pass


class RolUpdate(BaseModel):
    Nombre: Optional[str] = None
    Descripcion: Optional[str] = None
    Estatus: Optional[bool] = None
    Fecha_Actualizacion: Optional[datetime] = None


class Rol(RolBase):
    ID: UUID = Field(..., example="f47ac10b-58cc-4372-a567-0e02b2c3d479")

    class Config:
        orm_mode = True
