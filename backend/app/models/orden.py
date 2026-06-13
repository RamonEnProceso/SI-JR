from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base

class Orden(Base):
    __tablename__ = "ordenes"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    fecha_creacion: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    fecha_programada: Mapped[datetime] = mapped_column(TIMESTAMP)
    fecha_final: Mapped[datetime] = mapped_column(TIMESTAMP)
    
    direccion: Mapped[str] = mapped_column(String, nullable=False)
    descripcion: Mapped[str] = mapped_column(String)
    recomendacion: Mapped[str] = mapped_column(String)
    contacto_responsable: Mapped[str] = mapped_column(String)
    observaciones: Mapped[str] = mapped_column(String)
    
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    rubro_id: Mapped[int] = mapped_column(ForeignKey("orden_rubro.id"))
    estado_id: Mapped[int] = mapped_column(ForeignKey("orden_estado.id"))
    prioridad_id: Mapped[int] = mapped_column(ForeignKey("orden_prioridad.id"))
    
    cliente: Mapped["Cliente"] = relationship("Cliente", back_populates="ordenes")
    tecnicos: Mapped[list["OrdenTecnico"]] = relationship("OrdenTecnico", back_populates="orden")
    rubro: Mapped["OrdenRubro"] = relationship("OrdenRubro", back_populates="ordenes")
    estado: Mapped["OrdenEstado"] = relationship("OrdenEstado", back_populates="ordenes")
    prioridad: Mapped["OrdenPrioridad"] = relationship("OrdenPrioridad", back_populates="ordenes")
    checklist: Mapped["OrdenChecklist"] = relationship("OrdenChecklist", back_populates="orden")
    fotos: Mapped[list["OrdenFoto"]] = relationship("OrdenFoto", back_populates="orden")
    observaciones_detalladas: Mapped[list["OrdenObservacion"]] = relationship("OrdenObservacion", back_populates="orden")
    
    def __repr__(self):
        return f"Orden(id={self.id}, creacion='{self.fecha_creacion}', direccion='{self.direccion}')"
