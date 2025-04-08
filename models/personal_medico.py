"""Modelo y enumeraciones para el personal médico."""

import enum
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    DECIMAL,
    Enum as SqlEnum,
    func,
)
from config.db import Base


class EnumTipoPersonal(enum.Enum):
    """Enumeración de los tipos de personal médico."""
    MEDICO = "Médico"
    ENFERMERO = "Enfermero"
    ADMINISTRATIVO = "Administrativo"
    DIRECTIVO = "Directivo"
    APOYO = "Apoyo"
    RESIDENTE = "Residente"
    INTERNO = "Interno"


class EnumEstatus(enum.Enum):
    """Enumeración del estatus del personal médico."""
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"


class PersonalMedico(Base):
    """Modelo de la tabla tbb_personal_medico."""

    __tablename__ = "tbb_personal_medico"

    #Persona_ID = Column(Integer, ForeignKey("tbb_personas.ID"), primary_key=True, index=True)
    Persona_ID = Column(Integer, primary_key=True, index=True)
    Departamento_ID = Column(Integer)
    Cedula_Profesional = Column(String(100))
    Tipo = Column(SqlEnum(EnumTipoPersonal))
    Especialidad = Column(String(255))
    Fecha_Registro = Column(DateTime, default=func.now())
    Fecha_Contratacion = Column(DateTime)
    Fecha_Termino_Contrato = Column(DateTime)
    Salario = Column(DECIMAL(10, 2))
    Estatus = Column(SqlEnum(EnumEstatus))
    Fecha_Actualizacion = Column(DateTime)
