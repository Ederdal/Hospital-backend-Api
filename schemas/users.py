"""Esquemas Pydantic para operaciones con usuarios."""

from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Modelo base compartido por operaciones de usuario."""
    persona_id: UUID = Field(..., alias="Persona_ID")
    nombre_usuario: str = Field(..., alias="Nombre_Usuario")
    correo_electronico: EmailStr = Field(..., alias="Correo_Electronico")
    contrasena: str = Field(..., alias="Contrasena")
    numero_telefonico_movil: Optional[str] = Field(None, alias="Numero_Telefonico_Movil")
    estatus: str = Field(default="Activo", alias="Estatus")
    fecha_registro: Optional[datetime] = Field(None, alias="Fecha_Registro")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion")

    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
        from_attributes = True


class UserCreate(UserBase):
    """Modelo para crear un usuario."""
    pass


class UserUpdate(BaseModel):
    """Modelo para actualizar datos de un usuario."""
    persona_id: Optional[UUID] = Field(None, alias="Persona_ID")
    nombre_usuario: Optional[str] = Field(None, alias="Nombre_Usuario")
    correo_electronico: Optional[EmailStr] = Field(None, alias="Correo_Electronico")
    contrasena: Optional[str] = Field(None, alias="Contrasena")
    numero_telefonico_movil: Optional[str] = Field(None, alias="Numero_Telefonico_Movil")
    estatus: Optional[str] = Field(None, alias="Estatus")
    fecha_registro: Optional[datetime] = Field(None, alias="Fecha_Registro")
    fecha_actualizacion: Optional[datetime] = Field(None, alias="Fecha_Actualizacion")

    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
        from_attributes = True


class User(UserBase):
    """Modelo de respuesta al consultar un usuario."""
    id: UUID = Field(..., alias="ID")

    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
        from_attributes = True


class UserLogin(BaseModel):
    """Modelo para iniciar sesión."""
    nombre_usuario: Optional[str] = Field(None, alias="Nombre_Usuario")
    correo_electronico: Optional[EmailStr] = Field(None, alias="Correo_Electronico")
    contrasena: str = Field(..., alias="Contrasena")
    numero_telefonico_movil: Optional[str] = Field(None, alias="Numero_Telefonico_Movil")

    class Config:
        """Configuración del modelo."""
        allow_population_by_field_name = True
