from sqlalchemy import Column, Integer, Date, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Reservation(Base):
    __tablename__ = 'reservation'

    id_reservation = Column(Integer, primary_key=True, autoincrement=True)
    reservation_date = Column(Date, nullable=False)
    reservation_status = Column(Enum('attente', 'confirmee'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_book = Column(Integer, ForeignKey('book.id_book'), nullable=False)
