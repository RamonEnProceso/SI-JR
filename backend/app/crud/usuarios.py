from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.core.security import hash_password

def create_usuario(db: Session, usuario_load: UsuarioCreate):
    usuario = Usuario(
        nombre = usuario_load.nombre,
        email = usuario_load.email,
        rol_id = usuario_load.rol_id,
        password_hash = hash_password(usuario_load.password)
    )
    
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

def get_usuarios(db: Session):
    stmt = select(Usuario)
    return db.execute(stmt).scalars().all()

def get_usuario(db: Session, usuario_id:int):
    return db.get(Usuario, usuario_id)

def update_usuario(db: Session, usuario_load : UsuarioUpdate, usuario_id:int):
    usuario = db.get(Usuario, usuario_id)
    if usuario is None:
        return None
    
    if(usuario_load.nombre is not None):
        usuario.nombre = usuario_load.nombre
    if(usuario_load.email is not None):
        usuario.email = usuario_load.email
    if(usuario_load.password is not None):
        usuario.password_hash = hash_password(usuario_load.password)
    
    db.commit()
    db.refresh(usuario)
    return usuario

def delete_usuario (db: Session, usuario_id:int):

    usuario = db.get(Usuario, usuario_id)
    
    if usuario is None:
        return None
    
    db.delete(usuario)
    db.commit()
    return True

def get_ordenes (db: Session, usuario_id:int):

    usuario = db.get(Usuario, usuario_id)
    
    if usuario is None:
        return None
    
    return [ot.orden for ot in usuario.ordenes]