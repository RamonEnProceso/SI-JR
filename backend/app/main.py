from fastapi import FastAPI
from app.routers.roles import router as roles_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"online"}

app.include_router(roles_router)