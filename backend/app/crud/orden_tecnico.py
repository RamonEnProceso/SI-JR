from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Orden, Usuario, OrdenTecnico
from app.schemas.orden_tecnico import OrdenTecnicoCreate, OrdenTecnicoUpdate


def get_ordenes_tecnico(db: Session):
    stmt = select(OrdenTecnico)
    return db.execute(stmt).scalars().all()



def create_orden_tecnico(db: Session, data_load: OrdenTecnicoCreate):
    orden_tecnico = OrdenTecnico(
        orden_id = data_load.orden_id,
        tecnico_id = data_load.tecnico_id
    )
    
    db.add(orden_tecnico)
    db.commit()
    db.refresh(orden_tecnico)
    return orden_tecnico



def update_orden_tecnico(db: Session, orden_tecnico_id :int, data_load:OrdenTecnicoUpdate):
    orden_tecnico = db.get(OrdenTecnico, orden_tecnico_id)
    if(orden_tecnico is None):
        return None
    
    orden_tecnico.tecnico_id = data_load.tecnico_id
    
    db.commit()
    db.refresh(orden_tecnico)
    return orden_tecnico



def delete_orden_tecnico(db: Session, orden_tecnico_id :int):
    orden_tecnico = db.get(OrdenTecnico, orden_tecnico_id)
    if(orden_tecnico is None):
        return None
    
    db.delete(orden_tecnico)
    db.commit()
    return True



def get_tecnico(db: Session, orden_tecnico_id :int):
    orden_tecnico = db.get(OrdenTecnico, orden_tecnico_id)
    if(orden_tecnico is None):
        return None
    
    return orden_tecnico.tecnico



def get_orden(db: Session, orden_tecnico_id :int):
    orden_tecnico = db.get(OrdenTecnico, orden_tecnico_id)
    if(orden_tecnico is None):
        return None
    
    return orden_tecnico.orden
    
    
    
def get_ordenes_por_tecnico(db: Session, tecnico_id:int):
    tecnico = db.get(Usuario, tecnico_id)
    if tecnico is None:
        return None

    return tecnico.ordenes



def get_tecnicos_por_orden(db: Session, orden_id:int):
    orden = db.get(Orden, orden_id)
    if orden is None:
        return None

    return orden.tecnicos