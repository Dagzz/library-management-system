from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    __tablename__ = 'city'

    id_city = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
