from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import ForeignKey

class Adresse(Base):
    __tablename__ = 'adresse'

    id_adresse = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(10), nullable=False)
    street = Column(String(50), nullable=False)
    postal_code = Column(String(15), nullable=False)
    id_city = Column(Integer, ForeignKey('city.id_city'), nullable=False)
