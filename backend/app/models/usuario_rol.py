from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String

class UsuarioRol(Base):
    __tablename__ = "usuario_rol"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    usuarios: Mapped[list["Usuario"]] = relationship("Usuario", back_populates="rol")
    
    def __repr__(self):
        return f"UsuarioRol(id={self.id}, nombre='{self.nombre}')"