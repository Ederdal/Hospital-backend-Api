import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener la URL desde el archivo .env
database_url = os.getenv("SQLALCHEMY_DATABASE_URL")

if not database_url:
    raise ValueError("No se encontró la variable SQLALCHEMY_DATABASE_URL en el archivo .env")

print(f"🔌 Conectando a la base de datos local: {database_url}")

# Crear motor sin SSL
engine = create_engine(database_url)

# Crear sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarar base para los modelos
Base = declarative_base()

# Función para obtener la sesión en rutas y controladores
def get_db():
    """Provee una sesión de base de datos por solicitud."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
