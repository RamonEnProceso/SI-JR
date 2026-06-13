from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Integer

class ChecklistPlantillaItem(Base):
    __tablename__ = "checklist_plantilla_item"

    id: Mapped[int] = mapped_column(primary_key=True)
    plantilla_id: Mapped[int] = mapped_column(ForeignKey("checklist_plantilla.id"))
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    orden_visual: Mapped[int] = mapped_column(Integer)
    
    plantilla: Mapped["ChecklistPlantilla"] = relationship("ChecklistPlantilla", back_populates="items")
    
    def __repr__(self):
        return f"ChecklistPlantillaItem(id={self.id}, nombre='{self.nombre}')"