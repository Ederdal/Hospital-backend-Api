"""Esquemas Pydantic para la entidad Servicios Médicos."""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class ServiceMBase(BaseModel):
    nombre: str = Field(..., example="Consulta General")
    descripcion: Optional[str] = Field(None, example="Atención médica general para diagnóstico y evaluación.")
    observaciones: Optional[str] = Field(None, example="Disponible de lunes a viernes.")
    costo_servicio: int = Field(..., example=500)


class ServiceMCreate(ServiceMBase):
    pass


class ServiceMUpdate(BaseModel):
    nombre: Optional[str] = Field(None, example="Consulta Pediátrica")
    descripcion: Optional[str] = Field(None, example="Atención para niños y adolescentes.")
    observaciones: Optional[str] = Field(None, example="Solo turno matutino.")
    costo_servicio: Optional[int] = Field(None, example=700)
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-22T10:00:00.000Z")


class ServiceMResponse(ServiceMBase):
    id: UUID = Field(..., example="b3c7e9b2-8429-4c71-ae68-61c30269c237")
    fecha_registro: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")
    fecha_actualizacion: Optional[datetime] = Field(None, example="2025-03-21T22:19:44.610Z")

    class Config:
        orm_mode = True
