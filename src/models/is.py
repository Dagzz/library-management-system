from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Is(Base):
    __tablename__ = 'is'

    id_role = Column(Integer, ForeignKey('role.id_role'), primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'), primary_key=True)
