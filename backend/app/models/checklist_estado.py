from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

class ChecklistEstado(Base):
    __tablename__ = "checklist_estado"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    
    def __repr__(self):
        return f"ChecklistEstado(id={self.id}, nombre='{self.nombre}')"