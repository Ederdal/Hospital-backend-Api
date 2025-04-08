"""Modelo para la entidad Cita."""

import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Enum as SqlEnum,
)
from config.db import Base


class MyEstatusCita(enum.Enum):
    """Enumeración del estatus de la cita."""

    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    BLOQUEADO = "Bloqueado"
    SUSPENDIDO = "Suspendido"


class Cita(Base):
    """Modelo de la tabla tbb_citas."""

    __tablename__ = "tbb_citas"

    ID = Column(Integer, primary_key=True, index=True)
    #Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"))
    Persona_ID = Column(Integer)
    Hora_Cita = Column(DateTime)
    Telefono = Column(String(20))
    Correo_Electronico = Column(String(255))
    Motivo_Cita = Column(String(255))
    Estatus = Column(SqlEnum(MyEstatusCita))
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
