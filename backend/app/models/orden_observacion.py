from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import func
from datetime import datetime
from sqlalchemy import TIMESTAMP


class OrdenObservacion(Base):
    __tablename__ = "orden_observaciones"

    id: Mapped[int] = mapped_column(primary_key=True)
    orden_id: Mapped[int] = mapped_column(ForeignKey("ordenes.id"),nullable=False)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"),nullable=False)
    comentario: Mapped[str] = mapped_column(String, nullable=False)
    fecha_creacion: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    
    orden: Mapped["Orden"] = relationship("Orden", back_populates="observaciones_detalladas")
    tecnico: Mapped["Usuario"] = relationship("Usuario", back_populates="observaciones")
    
    def __repr__(self):
        return f"OrdenObservacion(id={self.id}, orden_id={self.orden_id}, comentario='{self.comentario}')"