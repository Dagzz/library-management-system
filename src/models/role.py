# ============================================
# Table: role
# ============================================

from sqlalchemy import Column, Integer, Text, String, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base
from .associations import user_role_table

class Role(Base):
    __tablename__ = 'role'
    __table_args__ = (
        UniqueConstraint('role_name', name='role_AK'),
    )

    id_role = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    role_name = Column(String(50), nullable=False)

    users = relationship(
        "User",
        secondary=user_role_table,
        back_populates="roles"
    )

    def __repr__(self):
        return f"<Role(id_role={self.id_role}, role_name='{self.role_name}')>"
