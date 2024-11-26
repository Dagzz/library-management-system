from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Collection(Base):
    __tablename__ = 'collection'

    id_collection = Column(Integer, primary_key=True, autoincrement=True)
    collection_name = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
