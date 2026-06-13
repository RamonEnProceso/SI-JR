from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import ForeignKey


class ChecklistPlantilla(Base):
    __tablename__ = "checklist_plantilla"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    rubro_id: Mapped[int] = mapped_column(ForeignKey("orden_rubro.id"),nullable=False)

    rubro: Mapped["OrdenRubro"] = relationship("OrdenRubro", back_populates="plantillas")
    items: Mapped[list["ChecklistPlantillaItem"]] = relationship("ChecklistPlantillaItem", back_populates="plantilla")
    checklist: Mapped[list["OrdenChecklist"]] = relationship("OrdenChecklist", back_populates="plantilla")
    
    def __repr__(self):
        return f"ChecklistPlantilla(id={self.id}, nombre='{self.nombre}', rubro_id={self.rubro_id})"