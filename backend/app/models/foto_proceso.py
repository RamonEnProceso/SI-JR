from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String


class FotoProceso(Base):
    __tablename__ = "fotos_proceso"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    
    fotos: Mapped[list["OrdenFoto"]] = relationship("OrdenFoto", back_populates="proceso")
    
    def __repr__(self):
        return f"FotoProceso(id={self.id}, nombre='{self.nombre}')"