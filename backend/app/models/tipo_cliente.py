from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

class TipoCliente(Base):
    __tablename__ = "tipo_cliente"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    clientes: Mapped[list["Cliente"]] = relationship("Cliente", back_populates="tipo")
    
    def __repr__(self):
        return f"TipoCLiente(id={self.id}, nombre='{self.nombre}')"