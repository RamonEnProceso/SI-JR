from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

class OrdenEstado(Base):
    __tablename__ = "orden_estado"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    ordenes: Mapped[list["Orden"]] = relationship("Orden", back_populates="estado")
    
    def __repr__(self):
        return f"OrdenEstado(id={self.id}, nombre='{self.nombre}')"