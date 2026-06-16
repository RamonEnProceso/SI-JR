from pydantic import BaseModel

class OrdenTecnicoCreate(BaseModel):
    orden_id : int
    tecnico_id : int

class OrdenTecnicoResponse(BaseModel):
    id: int
    orden_id : int
    tecnico_id : int

class OrdenTecnicoUpdate(BaseModel):
    tecnico_id : int