from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import UsuarioRol

def get_roles(db: Session):
    stmt = select(UsuarioRol)
    return db.execute(stmt).scalars().all()