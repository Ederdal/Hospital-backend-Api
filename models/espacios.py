"""Modelo ORM para representar los espacios físicos del hospital."""

import enum
import uuid
from datetime import datetime

from sqlalchemy import Column, String, Enum as SqlEnum, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from config.db import Base


class TipoEspacioEnum(str, enum.Enum):
    """Enumeración de tipos de espacios disponibles en el hospital."""

    CONSULTORIO = "Consultorio"
    LABORATORIO = "Laboratorio"
    QUIROFANO = "Quirófano"
    SALA_DE_ESPERA = "Sala de Espera"
    EDIFICIO = "Edificio"
    ESTACIONAMIENTO = "Estacionamiento"
    HABITACION = "Habitación"
    CAMA = "Cama"
    SALA_MATERNIDAD = "Sala Maternidad"
    CUNERO = "Cunero"
    ANFITEATRO = "Anfiteatro"
    OFICINA = "Oficina"
    SALA_DE_JUNTAS = "Sala de Juntas"
    AUDITORIO = "Auditorio"
    CAFETERIA = "Cafeteria"
    CAPILLA = "Capilla"
    FARMACIA = "Farmacia"
    VENTANILLA = "Ventanilla"
    RECEPCION = "Recepción"
    PISO = "Piso"


class EstatusEnum(str, enum.Enum):
    """Enumeración para el estatus del espacio."""

    ACTIVO = "Activo"
    INACTIVO = "Inactivo"


class Espacio(Base):
    """Modelo que representa un espacio físico dentro del hospital."""

    __tablename__ = "tbc_espacios"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    tipo = Column(SqlEnum(TipoEspacioEnum), nullable=False)
    nombre = Column(String(100), nullable=False)
    '''departamento_id = Column(
        String(36),
        ForeignKey("tbc_departamentos.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )'''
    departamento_id = Column(
        String(36),
        nullable=True,
        index=True,
    )
    estatus = Column(SqlEnum(EstatusEnum), nullable=False, default=EstatusEnum.ACTIVO)
    fecha_registro = Column(DateTime, default=datetime.utcnow)
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    capacidad = Column(Integer, nullable=True)
    espacio_superior_id = Column(
        String(36),
        ForeignKey("tbc_espacios.id", ondelete="SET NULL"),
        nullable=True,
    )

    servicios_medicos_espacios = relationship(
        "ServiciosMedicosEspacios",
        back_populates="espacio"
    )
