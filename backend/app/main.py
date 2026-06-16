from fastapi import FastAPI
from app.routers.roles import router as roles_router
from app.routers.tipos_cliente import router as tipos_cliente_router
from app.routers.rubros import router as rubros_router
from app.routers.clientes import router as clientes_router
from app.routers.ordenes import router as ordenes_router
from app.routers.usuarios import router as usuarios_router
from app.routers.orden_tecnico import router as orden_tecnico_router
from app import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"online"}

app.include_router(roles_router)
app.include_router(tipos_cliente_router)
app.include_router(rubros_router)
app.include_router(clientes_router)
app.include_router(ordenes_router)
app.include_router(usuarios_router)
app.include_router(orden_tecnico_router)