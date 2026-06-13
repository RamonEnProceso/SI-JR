from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from datetime import datetime
from sqlalchemy import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    rol_id: Mapped[int] = mapped_column(ForeignKey("usuario_rol.id"))
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    fecha_creacion: Mapped[datetime] = mapped_column(TIMESTAMP,server_default=func.now())
    
    rol: Mapped["UsuarioRol"] = relationship("UsuarioRol", back_populates="usuarios")
    ordenes: Mapped[list["OrdenTecnico"]] = relationship("OrdenTecnico", back_populates="tecnico")
    fotos: Mapped[list["OrdenFoto"]] = relationship("OrdenFoto", back_populates="tecnico")
    observaciones: Mapped[list["OrdenObservacion"]] = relationship("OrdenObservacion", back_populates="tecnico")
    
    def __repr__(self):
        return f"Usuario(id={self.id}, nombre='{self.nombre}', email='{self.email}', rol_id={self.rol_id})"
