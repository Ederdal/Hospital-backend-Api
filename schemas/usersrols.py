"""Esquemas Pydantic para la tabla intermedia usuario-rol."""

from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class UserRolBase(BaseModel):
    """Modelo base para asignación usuario-rol."""
    usuario_id: UUID = Field(..., alias="Usuario_ID")
    rol_id: UUID = Field(..., alias="Rol_ID")
    estatus: bool = Field(..., alias="Estatus")
    fecha_registro: Optional[datetime] = Field(None, alias="Fecha_Registro")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion")

    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
        from_attributes = True


class UserRolCreate(UserRolBase):
    """Modelo para crear una asignación de usuario a rol."""
    pass


class UserRolUpdate(BaseModel):
    """Modelo para actualizar una asignación existente."""
    estatus: Optional[bool] = Field(None, alias="Estatus")
    fecha_registro: Optional[datetime] = Field(None, alias="Fecha_Registro")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion")

    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
        from_attributes = True


class UserRol(UserRolBase):
    """Modelo de respuesta para asignación usuario-rol."""
    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
        from_attributes = True
