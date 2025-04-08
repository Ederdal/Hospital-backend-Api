"""Modelo para los servicios médicos del hospital."""

import uuid
from sqlalchemy import Column, String, Text, DateTime, Integer, func
from sqlalchemy.orm import relationship
from config.db import Base


class ServiceM(Base):
    """Modelo de la tabla tbc_servicios_medicos."""

    __tablename__ = "tbc_servicios_medicos"

    id = Column(String(36), primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
    observaciones = Column(Text, nullable=True)
    fecha_registro = Column(DateTime, nullable=False, server_default=func.now())
    fecha_actualizacion = Column(DateTime, nullable=True, onupdate=func.now())
    costo_servicio = Column(Integer, nullable=False)

    consumibles = relationship("ServiciosMedicosConsumibles", back_populates="servicio")
    espacios = relationship("ServiciosMedicosEspacios", back_populates="servicio")
