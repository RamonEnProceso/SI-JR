from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.orden_rubro import OrdenRubro

def get_rubros(db: Session):
    stmt = select(OrdenRubro)
    return db.execute(stmt).scalars().all()