from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Writes(Base):
    __tablename__ = 'writes'

    id_author = Column(Integer, ForeignKey('author.id_author'), primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id_book'), primary_key=True)
