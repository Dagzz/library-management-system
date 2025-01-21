# ============================================
# Table: modification
# ============================================

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Modification(Base):
    __tablename__ = 'modification'

    id_modif = Column(Integer, primary_key=True, autoincrement=True)
    date_modification = Column(DateTime, nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)

    book = relationship("Book", back_populates="modifications")
    user = relationship("User", back_populates="modifications")

    def __repr__(self):
        return f"<Modification(id_modif={self.id_modif}, date_modification={self.date_modification})>"
