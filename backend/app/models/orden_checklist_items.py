from app.db.base import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import String

class OrdenChecklistItem(Base):
    __tablename__ = "orden_checklist_items"

    id: Mapped[int] = mapped_column(primary_key=True)
    orden_checklist_id: Mapped[int] = mapped_column(ForeignKey("orden_checklist.id"),nullable=False)
    plantilla_item_id: Mapped[int] = mapped_column(ForeignKey("checklist_plantilla_item.id"))
    nombre: Mapped[str] = mapped_column(String, nullable=False)
    comentario: Mapped[str] = mapped_column(String)
    estado_id: Mapped[int] = mapped_column(ForeignKey("checklist_estado.id"),nullable=False,default=1)
    prioridad_id: Mapped[int] = mapped_column(ForeignKey("checklist_prioridad.id"),nullable=False,default=1)
    
    orden_checklist: Mapped["OrdenChecklist"] = relationship("OrdenChecklist", back_populates="items")
    plantilla_item: Mapped["ChecklistPlantillaItem"] = relationship("ChecklistPlantillaItem")
    
    
    def __repr__(self):
        return f"OrdenChecklistItem(id={self.id}, checklist_id={self.orden_checklist_id}, nombre='{self.nombre}')"