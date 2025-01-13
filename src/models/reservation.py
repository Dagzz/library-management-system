# ============================================
# Table: reservation
# ============================================

from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Reservation(Base):
    __tablename__ = 'reservation'
    __table_args__ = (
        UniqueConstraint('id_user', name='reservation_user_AK'),
    )

    id_reservation = Column(Integer, primary_key=True, autoincrement=True)
    reservation_date = Column(DateTime, nullable=False)
    is_confirmed = Column(Boolean, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)

    user = relationship("User", back_populates="reservations")
    book = relationship("Book", back_populates="reservations")

    def __repr__(self):
        return f"<Reservation(id_reservation={self.id_reservation}, is_confirmed={self.is_confirmed})>"
