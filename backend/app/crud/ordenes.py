from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Orden, OrdenPrioridad, OrdenEstado
from app.schemas.orden import OrdenCreate,OrdenUpdate

def create_orden(db: Session, ordenload: OrdenCreate):
    orden = Orden(
        fecha_programada = ordenload.fecha_programada,
        direccion = ordenload.direccion,
        descripcion = ordenload.descripcion,
        recomendacion = ordenload.recomendacion,
        cliente_id = ordenload.cliente_id,
        rubro_id = ordenload.rubro_id,
        estado_id = ordenload.estado_id,
        prioridad_id = ordenload.prioridad_id
    )
    
    db.add(orden)
    db.commit()
    db.refresh(orden)
    return orden

def get_ordenes(db: Session):
    stmt = select(Orden)
    return db.execute(stmt).scalars().all()

def get_orden(db: Session, orden_id:int):
    return db.get(Orden, orden_id)

def update_orden(db: Session, ordenload : OrdenUpdate, orden_id:int):
    orden = db.get(Orden, orden_id)
    if orden is None:
        return None

    datos_actualizados = ordenload.model_dump(exclude_unset=True)
    for campo, valor in datos_actualizados.items():
        setattr(orden, campo, valor)
    
    db.commit()
    db.refresh(orden)
    return orden

def delete_orden (db: Session, orden_id:int):

    orden = db.get(Orden, orden_id)
    
    if orden is None:
        return None
    
    db.delete(orden)
    db.commit()
    return True

def get_from_prioridad (db: Session, prioridad_id:int):
    prioridad = db.get(OrdenPrioridad, prioridad_id)
    if prioridad is None:
        return None
    
    return prioridad.ordenes

def get_from_estado (db: Session, estado_id:int):
    estado = db.get(OrdenEstado, estado_id)
    if estado is None:
        return None
    
    return estado.ordenes

def get_tecnicos(db: Session, orden_id:int):
    orden = db.get(Orden, orden_id)
    if orden is None:
        return None
    
    return [ot.tecnico for ot in orden.tecnicos]

def get_cliente(db: Session, orden_id:int):
    orden = db.get(Orden, orden_id)
    if orden is None:
        return None
    
    return orden.cliente