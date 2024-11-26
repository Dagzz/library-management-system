from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Enum, Date, ForeignKey

class User(Base):
    __tablename__ = 'user'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    mail = Column(String(254), nullable=False)
    phone = Column(String(15), nullable=False)
    login = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    last_connection_date = Column(Date, nullable=False)
    member_status = Column(Enum('actif', 'inactif'), nullable=False)
    id_adresse = Column(Integer, ForeignKey('adresse.id_adresse'))
