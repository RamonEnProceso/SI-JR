from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.get_usuarios_roles import get_roles

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
    )

@router.get("/")
def get_roles_route(db: Session = Depends(get_db)):
    
    return get_roles(db)