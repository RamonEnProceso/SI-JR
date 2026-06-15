from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ClienteCreate(BaseModel):
    nombre: str
    razon_social: str|None = None
    telefono: str
    email: str
    direccion: str
    tipo_cliente_id: int = 1
    contacto_responsable: str|None = None
    observaciones: str|None = None
    
class ClienteUpdate(BaseModel):
    nombre: str | None = None
    razon_social: str|None = None
    telefono: str | None = None
    email: str | None = None
    direccion: str | None = None
    tipo_cliente_id: int | None = None
    contacto_responsable: str|None = None
    observaciones: str|None = None
    
class ClienteResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    id: int
    nombre: str
    razon_social: str|None = None
    telefono: str
    email: str
    direccion: str
    tipo_cliente_id: int
    contacto_responsable: str|None = None
    observaciones: str|None = None
    creacion: datetime