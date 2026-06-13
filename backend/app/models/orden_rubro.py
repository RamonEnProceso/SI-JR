from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

class OrdenRubro(Base):
    __tablename__ = "orden_rubro"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    ordenes: Mapped[list["Orden"]] = relationship("Orden", back_populates="rubro")
    plantillas: Mapped[list["ChecklistPlantilla"]] = relationship("ChecklistPlantilla", back_populates="rubro")
    
    def __repr__(self):
        return f"OrdenRubro(id={self.id}, nombre='{self.nombre}')"