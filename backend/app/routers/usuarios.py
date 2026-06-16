from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.crud.usuarios import get_usuario, get_usuarios, create_usuario, delete_usuario, update_usuario, get_ordenes
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from app.schemas.orden import OrdenResponse

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/", response_model=list[UsuarioResponse])
def get_usuarios_route(db: Session = Depends(get_db)):
    return get_usuarios(db)

@router.get("/{usuario_id}", response_model=UsuarioResponse)
def get_usuario_route(
    usuario_id : int,
    db: Session = Depends(get_db)
    ):
    
    usuario = get_usuario(db, usuario_id)
    
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    
    return usuario

@router.post("/", response_model=UsuarioResponse)
def create_usuario_route(
    usuario_load:UsuarioCreate,
    db: Session = Depends(get_db)
    ):
    return create_usuario(db, usuario_load)

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def update_usuario_route(
    usuario_id : int,
    usuario_load: UsuarioUpdate,
    db: Session = Depends(get_db)
    ):
    
    usuario = update_usuario(db, usuario_load ,usuario_id)
    
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    
    return usuario

@router.delete("/{usuario_id}")
def delete_usuario_route(
    usuario_id : int,
    db: Session = Depends(get_db)
    ):
    usuario = delete_usuario(db, usuario_id)
    
    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    
    return {"message": f"Usuario {usuario_id} eliminado"}

@router.get("/{usuario_id}/ordenes", response_model=list[OrdenResponse])
def get_usuario_ordenes_route(
    usuario_id : int,
    db: Session = Depends(get_db)
    ):
    
    return get_ordenes(db, usuario_id)