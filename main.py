from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Universidad")

from app.estudiante_service.routers import router as estudiante_router
from app.carrera_service.routers import router as carrera_router
from app.facultad_service.routers import router as facultad_router

app.include_router(estudiante_router, prefix="/estudiantes")
app.include_router(carrera_router, prefix="/carreras")
app.include_router(facultad_router, prefix="/facultades")

@app.get("/", tags=["root"])
def root():
    return {"status": "ok", "services": ["/estudiantes", "/carreras", "/facultades"]}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
