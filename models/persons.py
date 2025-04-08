"""Modelo para la entidad Persona."""

from sqlalchemy import Column, Integer, String, DateTime, Boolean, Date
from config.db import Base


class Person(Base):
    """Modelo de la tabla tbb_personas."""

    __tablename__ = "tbb_personas"

    ID = Column(Integer, primary_key=True, index=True)
    Titulo_Cortesia = Column(String(20))
    Nombre = Column(String(100))
    Primer_Apellido = Column(String(100))
    Segundo_Apellido = Column(String(100))
    CURP = Column(String(18), unique=True, index=True)
    Correo_Electronico = Column(String(255), unique=True, index=True)
    Telefono = Column(String(20))
    Fecha_Nacimiento = Column(Date)
    Fotografia = Column(String(255))
    Genero = Column(String(20))
    Tipo_Sangre = Column(String(5))
    Estatus = Column(Boolean)
    Fecha_Registro = Column(DateTime)
    Fecha_Actualizacion = Column(DateTime)
