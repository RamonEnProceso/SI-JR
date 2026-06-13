from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import func
from datetime import datetime
from sqlalchemy import TIMESTAMP


class OrdenFoto(Base):
    __tablename__ = "orden_fotos"

    id: Mapped[int] = mapped_column(primary_key=True)
    orden_id: Mapped[int] = mapped_column(ForeignKey("ordenes.id"),nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"),nullable=False)
    path: Mapped[str] = mapped_column(String, nullable=False)
    proceso_id: Mapped[int] = mapped_column(ForeignKey("fotos_proceso.id"),nullable=False)
    fecha_subida: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    
    orden: Mapped["Orden"] = relationship("Orden", back_populates="fotos")
    tecnico: Mapped["Usuario"] = relationship("Usuario", back_populates="fotos")
    proceso: Mapped["FotoProceso"] = relationship("FotoProceso", back_populates="fotos")
    
    def __repr__(self):
        return f"OrdenFoto(id={self.id}, orden_id={self.orden_id}, path='{self.path}')"