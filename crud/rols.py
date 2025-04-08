"""DAO para la gestión de roles en la base de datos."""

from sqlalchemy.orm import Session
from models import rols as rol_model
from schemas import rols as rol_schema


def get_rol(db: Session, rol_id: str):
    return db.query(rol_model.Rol).filter(rol_model.Rol.ID == rol_id).first()


def get_rol_by_nombre(db: Session, nombre: str):
    return db.query(rol_model.Rol).filter(rol_model.Rol.Nombre == nombre).first()


def get_rols(db: Session, skip: int = 0, limit: int = 10):
    return db.query(rol_model.Rol).offset(skip).limit(limit).all()


def create_rol(db: Session, rol: rol_schema.RolCreate):
    db_rol = rol_model.Rol(
        Nombre=rol.Nombre,
        Descripcion=rol.Descripcion,
        Estatus=rol.Estatus,
        Fecha_Registro=rol.Fecha_Registro,
        Fecha_Actualizacion=rol.Fecha_Actualizacion
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol


def update_rol(db: Session, rol_id: str, rol: rol_schema.RolUpdate):
    db_rol = db.query(rol_model.Rol).filter(rol_model.Rol.ID == rol_id).first()
    if db_rol:
        for var, value in rol.dict(exclude_unset=True).items():
            setattr(db_rol, var, value)
        db.commit()
        db.refresh(db_rol)
    return db_rol


def delete_rol(db: Session, rol_id: str):
    db_rol = db.query(rol_model.Rol).filter(rol_model.Rol.ID == rol_id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol
