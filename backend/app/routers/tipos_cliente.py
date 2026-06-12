from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.get_tipos_cliente import get_tipo_clientes

router = APIRouter()

@router.get("/tipos_cliente")
def get_tipo_clientes_route(db: Session = Depends(get_db)):
    
    return get_tipo_clientes(db)