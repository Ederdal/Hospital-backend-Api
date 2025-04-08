"""API principal para Hospital S.A. de C.V."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.db import Base, engine
import models  # Importa todos los modelos definidos

# Routers activos
from routes.users import users_router
from routes.persons import persons_router
from routes.servicios_medicos import serviceM
from routes.espacios import espacio
from routes.userrol import userrol
from routes.rol import rol

# FastAPI app initialization
app = FastAPI(
    title="HOSPITAL S.A. de C.V.",
    description="API RESTful para la gestión operativa de un hospital, construida con FastAPI y SQLAlchemy.",
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de rutas activas
app.include_router(users_router)
app.include_router(persons_router)
app.include_router(serviceM)
app.include_router(espacio)
app.include_router(rol)
app.include_router(userrol)

# Creación de las tablas después de incluir los routers
print("🔄 Creando las tablas en MySQL si no existen...")
Base.metadata.create_all(bind=engine)
print("✅ Tablas creadas exitosamente en MySQL")
