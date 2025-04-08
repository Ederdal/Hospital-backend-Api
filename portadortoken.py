"""Middleware para validación de JWT y autorización."""

from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from jwt_config import valida_token
from crud import users as crud_users
from config.db import get_db


class Portador(HTTPBearer):
    """Clase de autorización basada en token JWT."""

    async def __call__(self, request: Request):
        """Intercepta y valida el token JWT en el encabezado."""
        autorizacion = await super().__call__(request)
        datos_token = valida_token(autorizacion.credentials)

        # Obtener sesión de base de datos
        db: Session = next(get_db())

        # Validar existencia del usuario
        db_user = crud_users.get_user_by_username(db, username=datos_token["Nombre_Usuario"])
        if db_user is None:
            raise HTTPException(status_code=404, detail="LogIn incorrecto")

        return db_user
