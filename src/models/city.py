# ============================================
# Table: city
# ============================================

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class City(Base):
    __tablename__ = 'city'

    id_city = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    addresses = relationship("Address", back_populates="city")

    def __repr__(self):
        return f"<City(id_city={self.id_city}, name='{self.name}')>"
