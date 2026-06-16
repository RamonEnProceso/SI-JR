from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.orden_tecnico import get_orden, get_tecnico, create_orden_tecnico, update_orden_tecnico, delete_orden_tecnico, get_ordenes_tecnico
from app.schemas.orden_tecnico import OrdenTecnicoCreate, OrdenTecnicoResponse, OrdenTecnicoUpdate
from app.schemas.orden import OrdenResponse
from app.schemas.usuario import UsuarioResponse

router = APIRouter(
    prefix="/orden_tecnico",
    tags=["Orden-Tecnico"]
)


@router.get("/orden/{orden_tecnico_id}", response_model=OrdenResponse)
def get_orden_route(
    orden_tecnico_id : int,
    db: Session = Depends(get_db)
    ):
    
    orden = get_orden(db, orden_tecnico_id)
    if orden is None:
        raise HTTPException(
            status_code=404,
            detail="Orden no encontrada"
        )
    return orden

@router.get("/tecnico/{orden_tecnico_id}", response_model=UsuarioResponse)
def get_tecnico_route(
    orden_tecnico_id : int,
    db: Session = Depends(get_db)
    ):
    
    tecnico = get_tecnico(db, orden_tecnico_id)
    if tecnico is None:
        raise HTTPException(
            status_code=404,
            detail="Tecnico no encontrado"
        )
    
    return tecnico

@router.get("/", response_model = list[OrdenTecnicoResponse])
def get_ordenes_tecnico_route(db: Session = Depends(get_db)):
    return get_ordenes_tecnico(db)




@router.post("/", response_model=OrdenTecnicoResponse)
def create_orden_tecnico_route(
    data_load:OrdenTecnicoCreate,
    db: Session = Depends(get_db)
    ):
    return create_orden_tecnico(db, data_load)

@router.put("/{orden_tecnico_id}", response_model=OrdenTecnicoResponse)
def update_orden_tecnico_route(
    orden_tecnico_id : int,
    data_load: OrdenTecnicoUpdate,
    db: Session = Depends(get_db)
    ):
    
    orden_tecnico = update_orden_tecnico(db,orden_tecnico_id,data_load)
    
    if orden_tecnico is None:
        raise HTTPException(
            status_code=404,
            detail="Relacion OrdenTecnico no encontrada"
        )
    
    return orden_tecnico

@router.delete("/{orden_tecnico_id}")
def delete_orden_tecnico_route(
    orden_tecnico_id : int,
    db: Session = Depends(get_db)
    ):
    orden_tecnico = delete_orden_tecnico(db, orden_tecnico_id)
    
    if orden_tecnico is None:
        raise HTTPException(
            status_code=404,
            detail="Relacion OrdenTecnico no encontrada"
        )
    
    return {"message": f"Relacion OrdenTecnico {orden_tecnico_id} eliminada"}