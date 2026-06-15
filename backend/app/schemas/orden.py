from pydantic import BaseModel, ConfigDict
from datetime import datetime

class OrdenCreate(BaseModel):
    cliente_id: int
    fecha_programada: datetime | None = None
    rubro_id: int = 1
    direccion: str 
    descripcion: str | None = None
    recomendacion: str | None = None
    estado_id: int = 1
    prioridad_id: int = 1
    
class OrdenUpdate(BaseModel):
    fecha_programada: datetime | None = None
    fecha_final: datetime | None = None
    rubro_id: int | None = None
    direccion:str | None = None
    descripcion:str | None = None
    recomendacion:str | None = None
    estado_id: int | None = None
    prioridad_id: int | None = None
    
class OrdenResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )
    
    id: int
    cliente_id: int
    fecha_creacion: datetime
    fecha_programada: datetime | None = None
    fecha_final: datetime | None = None
    rubro_id: int
    direccion:str 
    descripcion:str | None = None
    recomendacion:str | None = None
    estado_id: int
    prioridad_id: int