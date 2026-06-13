from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

class OrdenChecklist(Base):
    __tablename__ = "orden_checklist"

    id: Mapped[int] = mapped_column(primary_key=True)
    orden_id: Mapped[int] = mapped_column(ForeignKey("ordenes.id"),nullable=False)
    plantilla_id: Mapped[int] = mapped_column(ForeignKey("checklist_plantilla.id"))
    
    orden: Mapped["Orden"] = relationship("Orden", back_populates="checklist")
    plantilla: Mapped["ChecklistPlantilla"] = relationship("ChecklistPlantilla", back_populates="checklist")
    items: Mapped[list["OrdenChecklistItem"]] = relationship("OrdenChecklistItem", back_populates="orden_checklist")
    
    def __repr__(self):
        return f"OrdenChecklist(id={self.id}, orden_id={self.orden_id}, plantilla_id={self.plantilla_id})"