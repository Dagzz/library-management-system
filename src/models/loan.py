from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Loan(Base):
    __tablename__ = 'loan'

    id_loan = Column(Integer, primary_key=True, autoincrement=True)
    date_loan = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)
