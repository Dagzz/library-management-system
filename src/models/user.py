# ============================================ 
# Table: user
# ============================================

from sqlalchemy import (
    Column, Index, Integer, String, Boolean,
    DateTime, ForeignKey, UniqueConstraint
)
from sqlalchemy.orm import relationship
from .base import Base
from .associations import user_role_table

class User(Base):
    __tablename__ = 'user'
    __table_args__ = (
        UniqueConstraint('login', name='user_AK'),
        Index('user_Idx', 'last_name', 'mail'),
    )

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    phone = Column(String(15), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    last_connection_date = Column(DateTime, nullable=False)
    is_active = Column(Boolean, nullable=False)
    login = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    mail = Column(String(254), nullable=False)
    id_address = Column(Integer, ForeignKey('address.id_address'))

    address = relationship("Address", back_populates="users")
    roles = relationship(
        "Role",
        secondary=user_role_table,
        back_populates="users"
    )
    loans = relationship("Loan", back_populates="user")
    reservations = relationship("Reservation", back_populates="user")
    modifications = relationship("Modification", back_populates="user")
    authentication = relationship(
        "Authentication", back_populates="user", uselist=False
    )

    def __repr__(self):
        return f"<User(id_user={self.id_user}, login='{self.login}')>"
