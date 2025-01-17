# ============================================
# Table: authentication
# ============================================

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Authentication(Base):
    __tablename__ = 'authentication'

    id_authentication = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    login = Column(String(100), nullable=False, unique=True)
    hashed_password = Column(String(255), nullable=False)

    user = relationship("User", back_populates="authentication")

    def __repr__(self):
        return f"<Authentication(id_authentication={self.id_authentication}, login={self.login})>"
