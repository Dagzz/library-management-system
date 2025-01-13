# ============================================
# Table: language
# ============================================

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Language(Base):
    __tablename__ = 'language'

    id_language = Column(Integer, primary_key=True, autoincrement=True)
    language_name = Column(String(50), nullable=False)

    books = relationship("Book", back_populates="language")

    def __repr__(self):
        return f"<Language(id_language={self.id_language}, language_name='{self.language_name}')>"
