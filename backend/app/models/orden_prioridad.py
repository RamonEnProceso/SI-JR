from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

class OrdenPrioridad(Base):
    __tablename__ = "orden_prioridad"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    ordenes: Mapped[list["Orden"]] = relationship("Orden", back_populates="prioridad")
    
    def __repr__(self):
        return f"OrdenPrioridad(id={self.id}, nombre='{self.nombre}')"