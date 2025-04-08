"""Modelo para la entidad Rol."""

import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from config.db import Base


class Rol(Base):
    """Modelo de la tabla tbc_roles."""

    __tablename__ = "tbc_roles"

    ID = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    Nombre = Column(String(60), nullable=False)
    Descripcion = Column(LONGTEXT, nullable=True)
    Estatus = Column(Boolean, nullable=True)
    Fecha_Registro = Column(DateTime, nullable=True)
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    usuarios_roles = relationship("UserRol", back_populates="rol")
