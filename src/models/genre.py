from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Genre(Base):
    __tablename__ = 'genre'

    id_genre = Column(Integer, primary_key=True, autoincrement=True)
    name_genre = Column(String(100), nullable=False)
