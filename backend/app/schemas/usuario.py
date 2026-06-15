from pydantic import BaseModel, ConfigDict
from datetime import datetime

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    rol_id: int = 2
    password: str
    
class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: str | None = None
    password: str | None = None
    
class UsuarioResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    id: int
    nombre: str
    email: str
    rol_id: int
    fecha_creacion: datetime