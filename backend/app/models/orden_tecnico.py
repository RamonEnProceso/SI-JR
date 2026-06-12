from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

class OrdenTecnico(Base):
    __tablename__ = "orden_tecnico"

    id: Mapped[int] = mapped_column(primary_key=True)
    orden_id: Mapped[int] = mapped_column(ForeignKey("ordenes.id"),nullable=False)
    tecnico_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"),nullable=False)
    
    orden: Mapped["Orden"] = relationship("Orden", back_populates="tecnicos")
    tecnico: Mapped["Usuario"] = relationship("Usuario", back_populates="ordenes")
    
    def __repr__(self):
        return f"OrdenTecnico(id={self.id}, orden='{self.orden_id}')"