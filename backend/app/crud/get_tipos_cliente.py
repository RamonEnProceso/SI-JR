from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import TipoCliente

def get_tipo_clientes(db: Session):
    stmt = select(TipoCliente)
    return db.execute(stmt).scalars().all()