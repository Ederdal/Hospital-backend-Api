"""Modelo SQLAlchemy para la tabla de usuarios."""

import enum
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, text
from sqlalchemy.orm import relationship
from config.db import Base


class MyEstatus(str, enum.Enum):
    """Enumeración de estados para el usuario."""
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    BLOQUEADO = "Bloqueado"
    SUSPENDIDO = "Suspendido"


class User(Base):
    """Modelo ORM para los usuarios del sistema."""
    __tablename__ = "tbb_usuarios"

    id = Column("ID", String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    #persona_id = Column("Persona_ID", String(36), ForeignKey("tbb_personas.ID"), nullable=False)
    persona_id = Column("Persona_ID", String(36), nullable=False)
    nombre_usuario = Column("Nombre_Usuario", String(60), unique=True, nullable=False)
    correo_electronico = Column("Correo_Electronico", String(100), unique=True, nullable=False)
    contrasena = Column("Contrasena", String(255), nullable=False)
    numero_telefonico_movil = Column("Numero_Telefonico_Movil", String(20), nullable=True)
    estatus = Column("Estatus", Enum(MyEstatus), default=MyEstatus.ACTIVO, nullable=False)
    fecha_registro = Column("Fecha_Registro", DateTime, nullable=False,
                            server_default=text('CURRENT_TIMESTAMP'))
    fecha_actualizacion = Column(
        "Fecha_Actualizacion",
        DateTime,
        nullable=True,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    persona = relationship("Person", back_populates="usuario")
