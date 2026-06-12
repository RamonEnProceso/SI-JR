from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    razon_social: Mapped[str] = mapped_column(String)
    telefono: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True)
    direccion: Mapped[str] = mapped_column(String, nullable=False)
    tipo_cliente_id: Mapped[int] = mapped_column(ForeignKey("tipo_cliente.id"))
    contacto_responsable: Mapped[str] = mapped_column(String)
    observaciones: Mapped[str] = mapped_column(String)
    creacion: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
    
    tipo: Mapped["TipoCliente"] = relationship("TipoCliente", back_populates="clientes")
    
    ordenes: Mapped[list["Orden"]] = relationship("Orden", back_populates="cliente")
    
    def __repr__(self):
        return f"Cliente(id={self.id}, nombre='{self.nombre}', telefono='{self.telefono}', email='{self.email}', tipo='{self.tipo_cliente_id}')"
