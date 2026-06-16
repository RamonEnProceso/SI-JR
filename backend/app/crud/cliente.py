from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models import Cliente
from app.schemas.cliente import ClienteCreate, ClienteUpdate

def create_cliente(db: Session, cliente: ClienteCreate):
    clienteDB = Cliente(
        nombre = cliente.nombre,
        razon_social = cliente.razon_social,
        telefono = cliente.telefono,
        email = cliente.email,
        direccion = cliente.direccion,
        tipo_cliente_id = cliente.tipo_cliente_id,
        contacto_responsable = cliente.contacto_responsable,
        observaciones = cliente.observaciones
    )
    db.add(clienteDB)
    db.commit()
    db.refresh(clienteDB)
    return clienteDB

def get_clientes(db: Session):
    stmt = select(Cliente)
    return db.execute(stmt).scalars().all()

def get_cliente(db: Session, cliente_id:int):
    return db.get(Cliente, cliente_id)
        


def update_cliente(db: Session, cliente: ClienteUpdate, cliente_id: int):
    clienteDB = db.get(Cliente, cliente_id)
    if clienteDB is None:
        return None

    datos_actualizados = cliente.model_dump(exclude_unset=True)
    for campo, valor in datos_actualizados.items():
        setattr(clienteDB, campo, valor)
    
    db.commit()
    db.refresh(clienteDB)
    return clienteDB

def delete_cliente (db: Session, cliente_id:int):

    cliente = db.get(Cliente, cliente_id)
    
    if cliente is None:
        return None
    
    db.delete(cliente)
    db.commit()
    return True

def get_ordenes(db: Session, cliente_id: int):
    cliente = db.get(Cliente, cliente_id)
    if cliente is None:
        return None

    return cliente.ordenes