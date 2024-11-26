from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Belongs(Base):
    __tablename__ = 'belongs'

    id_genre = Column(Integer, ForeignKey('genre.id_genre'), primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id_book'), primary_key=True)
