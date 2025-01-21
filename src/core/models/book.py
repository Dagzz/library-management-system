# ============================================
# Table: book
# ============================================

from sqlalchemy import (
    Column, Integer, String, DateTime, Text, ForeignKey, Enum
)
from sqlalchemy.orm import relationship
from .base import Base
from .associations import writes_table, genre_book_table

class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    publication_date = Column(DateTime)
    status = Column(
        Enum("available", "borrowed", "reserved", name="status_enum"),
        nullable=False
    )
    aspect = Column(
        Enum("new", "good", "damaged", name="aspect_enum"),
        nullable=False
    )
    isbn = Column(String(17), nullable=False)
    page_number = Column(Integer, nullable=False)
    editor = Column(String(255), nullable=False)
    resume = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime)
    id_collection = Column(Integer, ForeignKey('collection.id_collection'), nullable=False)
    id_language = Column(Integer, ForeignKey('language.id_language'), nullable=False)

    authors = relationship("Author", secondary=writes_table, back_populates="books")
    genres = relationship("Genre", secondary=genre_book_table, back_populates="books")
    collection = relationship("Collection", back_populates="books")
    language = relationship("Language", back_populates="books")

    loans = relationship("Loan", back_populates="book")
    reservations = relationship("Reservation", back_populates="book")
    modifications = relationship("Modification", back_populates="book")

    def __repr__(self):
        return f"<Book(id_book={self.id_book}, title='{self.title}')>"
