from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.get_rubros import get_rubros

router = APIRouter()

@router.get("/rubros")
def get_tipo_clientes_route(db: Session = Depends(get_db)):
    
    return get_rubros(db)