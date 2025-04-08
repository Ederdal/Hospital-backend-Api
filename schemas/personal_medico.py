"""Esquemas Pydantic para la entidad Personal Médico."""

from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from models.personal_medico import EnumTipoPersonal, EnumEstatus


class PersonalMedicoBase(BaseModel):
    """Campos base para un registro de personal médico."""
    Persona_ID: int
    Departamento_ID: int
    Cedula_Profesional: str
    Tipo: EnumTipoPersonal
    Especialidad: str
    Fecha_Contratacion: datetime
    Fecha_Termino_Contrato: datetime
    Salario: Decimal
    Estatus: EnumEstatus


class PersonalMedicoCreate(PersonalMedicoBase):
    """Esquema para la creación de un registro de personal médico."""


class PersonalMedicoUpdate(BaseModel):
    """Esquema para la actualización parcial de un registro de personal médico."""
    Departamento_ID: Optional[int] = None
    Cedula_Profesional: Optional[str] = None
    Tipo: Optional[EnumTipoPersonal] = None
    Especialidad: Optional[str] = None
    Fecha_Contratacion: Optional[datetime] = None
    Fecha_Termino_Contrato: Optional[datetime] = None
    Salario: Optional[Decimal] = None
    Estatus: Optional[EnumEstatus] = None
    Fecha_Actualizacion: Optional[datetime] = None


class PersonalMedicoResponse(PersonalMedicoBase):
    """Esquema de respuesta para un registro de personal médico."""
    Fecha_Registro: Optional[datetime] = None
    Fecha_Actualizacion: Optional[datetime] = None

    class Config:
        orm_mode = True
