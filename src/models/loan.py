# ============================================
# Table: loan
# ============================================

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class Loan(Base):
    __tablename__ = 'loan'

    id_loan = Column(Integer, primary_key=True, autoincrement=True)
    date_loan = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)

    user = relationship("User", back_populates="loans")
    book = relationship("Book", back_populates="loans")

    def __repr__(self):
        return f"<Loan(id_loan={self.id_loan}, date_loan={self.date_loan}, return_date={self.return_date})>"
