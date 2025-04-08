"""Modelo SQLAlchemy para la tabla tbd_usuarios_roles."""

from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from config.db import Base


class UserRol(Base):
    """Modelo de relación usuario-rol (tabla intermedia)."""
    __tablename__ = "tbd_usuarios_roles"

    usuario_id = Column("Usuario_ID", String(36), ForeignKey("tbb_usuarios.ID"), primary_key=True)
    rol_id = Column("Rol_ID", String(36), ForeignKey("tbc_roles.ID"), primary_key=True)
    estatus = Column("Estatus", Boolean, nullable=True)
    fecha_registro = Column("Fecha_Registro", DateTime, nullable=True)
    fecha_actualizacion = Column("Fecha_Actualizacion", DateTime, nullable=True)

    rol = relationship("Rol", back_populates="usuarios_roles")
