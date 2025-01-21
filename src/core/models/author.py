# ============================================
# Table: author
# ============================================

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .base import Base
from .associations import writes_table

class Author(Base):
    __tablename__ = 'author'

    id_author = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    bio = Column(Text, nullable=False)

    books = relationship("Book", secondary=writes_table, back_populates="authors")

    def __repr__(self):
        return f"<Author(id_author={self.id_author}, name='{self.first_name} {self.last_name}')>"
