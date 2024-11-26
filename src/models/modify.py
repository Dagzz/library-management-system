from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Modify(Base):
    __tablename__ = 'modify'

    id_user = Column(Integer, ForeignKey('user.id_user'), primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id_book'), primary_key=True)
    modification_date = Column(DateTime, nullable=False)
