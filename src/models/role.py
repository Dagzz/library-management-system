from sqlalchemy import Column, Integer, Enum, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Role(Base):
    __tablename__ = 'role'

    id_role = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(Enum('administrateur', 'membre', 'super_administrateur'), nullable=False)
    description = Column(Text, nullable=False)
