"""Manejo de generación y validación de tokens JWT."""

from jwt import encode as jwt_encode, decode as jwt_decode


def solicita_token(dato: dict) -> str:
    """Genera un token JWT con los datos proporcionados."""
    return jwt_encode(payload=dato, key="pozoles", algorithm="HS256")


def valida_token(token: str) -> dict:
    """Valida y decodifica un token JWT."""
    return jwt_decode(token, key="pozoles", algorithms=["HS256"])
