from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from estudiante_service.main import app as estudiantes_app
from carrera_service.main import app as carreras_app
from facultad_service.main import app as facultades_app

app = FastAPI(
    title="Universidad API",
    version="1.0.0",
    description="API unificada con sub-aplicaciones: /estudiantes, /carreras, /facultades",
)

# (Opcional) CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/estudiantes", estudiantes_app)
app.mount("/carreras", carreras_app)
app.mount("/facultades", facultades_app)

@app.get("/", tags=["root"])
def root():
    return {
        "name": "Universidad API",
        "endpoints": {
            "estudiantes": "/estudiantes",
            "carreras": "/carreras",
            "facultades": "/facultades",
            "docs": {
                "estudiantes": "/estudiantes/docs",
                "carreras": "/carreras/docs",
                "facultades": "/facultades/docs",
            },
        },
    }
