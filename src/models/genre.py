# ============================================
# Table: genre
# ============================================

from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base
from .associations import genre_book_table

class Genre(Base):
    __tablename__ = 'genre'
    __table_args__ = (
        UniqueConstraint('name_genre', name='genre_AK'),
    )

    id_genre = Column(Integer, primary_key=True, autoincrement=True)
    name_genre = Column(String(100), nullable=False)

    books = relationship("Book", secondary=genre_book_table, back_populates="genres")

    def __repr__(self):
        return f"<Genre(id_genre={self.id_genre}, name_genre='{self.name_genre}')>"
