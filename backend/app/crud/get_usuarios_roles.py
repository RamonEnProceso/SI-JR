from app.db.dependencies import get_db
from sqlalchemy import select
from fastapi import Depends
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.models.usuario_rol import UsuarioRol

def get_roles(db: Session):
    stmt = select(UsuarioRol)
    return db.execute(stmt).scalars().all()