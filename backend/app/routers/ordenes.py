from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.ordenes import create_orden, get_orden, get_ordenes, update_orden, delete_orden, get_from_estado, get_from_prioridad, get_cliente, get_tecnicos
from app.schemas.orden import OrdenCreate, OrdenResponse, OrdenUpdate
from app.schemas.usuario import UsuarioResponse
from app.schemas.cliente import ClienteResponse

router = APIRouter(
    prefix="/ordenes",
    tags=["Ordenes"]
)

@router.get("/", response_model=list[OrdenResponse])
def get_ordenes_route(db: Session = Depends(get_db)):
    return get_ordenes(db)

@router.get("/{orden_id}", response_model=OrdenResponse)
def get_orden_route(
    orden_id : int,
    db: Session = Depends(get_db)
    ):
    
    orden = get_orden(db, orden_id)
    
    if orden is None:
        raise HTTPException(
            status_code=404,
            detail="Orden no encontrada"
        )
    
    return orden

@router.post("/", response_model=OrdenResponse)
def create_orden_route(
    orden_load:OrdenCreate,
    db: Session = Depends(get_db)
    ):
    return create_orden(db, orden_load)

@router.put("/{orden_id}", response_model=OrdenResponse)
def update_orden_route(
    orden_id : int,
    orden_post: OrdenUpdate,
    db: Session = Depends(get_db)
    ):
    
    orden = update_orden(db, orden_post, orden_id)
    
    if orden is None:
        raise HTTPException(
            status_code=404,
            detail="Orden no encontrada"
        )
    
    return orden

@router.delete("/{orden_id}")
def delete_orden_route(
    orden_id : int,
    db: Session = Depends(get_db)
    ):
    orden = delete_orden(db, orden_id)
    
    if orden is None:
        raise HTTPException(
            status_code=404,
            detail="Orden no encontrada"
        )
    
    return {"message": f"Orden {orden_id} eliminada"}




@router.get("/prioridad/{prioridad_id}", response_model=list[OrdenResponse])
def get_from_prioridad_route(
    prioridad_id:int, 
    db: Session = Depends(get_db)
    ):
    return get_from_prioridad(db,prioridad_id)

@router.get("/estado/{estado_id}", response_model=list[OrdenResponse])
def get_from_estado_route(
    estado_id:int, 
    db: Session = Depends(get_db)
    ):
    return get_from_estado(db,estado_id)




@router.get("/{orden_id}/tecnicos", response_model=list[UsuarioResponse])
def get_tecnicos_route(
    orden_id : int,
    db: Session = Depends(get_db)
    ):
    return get_tecnicos(db, orden_id)

@router.get("/{orden_id}/cliente", response_model=ClienteResponse)
def get_cliente_route(
    orden_id : int,
    db: Session = Depends(get_db)
    ):
    return get_cliente(db, orden_id)