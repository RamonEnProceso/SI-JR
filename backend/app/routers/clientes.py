from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.cliente import create_cliente,update_cliente,get_cliente,get_clientes,delete_cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate, ClienteResponse

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

@router.get("/", response_model=list[ClienteResponse])
def get_clientes_route(db: Session = Depends(get_db)):
    return get_clientes(db)

@router.get("/{cliente_id}", response_model=ClienteResponse)
def get_cliente_route(
    cliente_id : int,
    db: Session = Depends(get_db)
    ):
    
    cliente = get_cliente(db, cliente_id)
    
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )
    
    return cliente

@router.post("/", response_model=ClienteResponse)
def create_cliente_route(
    cliente:ClienteCreate,
    db: Session = Depends(get_db)
    ):
    return create_cliente(db, cliente)

@router.put("/{cliente_id}", response_model=ClienteResponse)
def update_cliente_route(
    cliente_id : int,
    cliente_post: ClienteUpdate,
    db: Session = Depends(get_db)
    ):
    
    cliente = update_cliente(db, cliente_post ,cliente_id)
    
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )
    
    return cliente

@router.delete("/{cliente_id}")
def delete_cliente_route(
    cliente_id : int,
    db: Session = Depends(get_db)
    ):
    cliente = delete_cliente(db, cliente_id)
    
    if cliente is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )
    
    return {"message": f"Cliente {cliente_id} eliminado"}