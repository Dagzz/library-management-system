# ============================================
# Table: address
# ============================================

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Address(Base):
    __tablename__ = 'address'

    id_address = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(10), nullable=False)
    street = Column(String(50), nullable=False)
    postal_code = Column(String(15), nullable=False)
    id_city = Column(Integer, ForeignKey('city.id_city'), nullable=False)

    city = relationship("City", back_populates="addresses")
    users = relationship("User", back_populates="address")

    def __repr__(self):
        return (
            f"<Address(id_address={self.id_address}, number='{self.number}', "
            f"street='{self.street}', postal_code='{self.postal_code}')>"
        )
