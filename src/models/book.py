from sqlalchemy import Column, Integer, String, Text, Enum, DateTime, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Book(Base):
    __tablename__ = 'book'

    id_book = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    publication_date = Column(Date)
    status = Column(Enum('disponible', 'emprunte', 'reserve'), nullable=False)
    condition = Column(Enum('neuf', 'bon', 'abime'), nullable=False)
    isbn = Column(String(17), nullable=False)
    page_number = Column(Integer, nullable=False)
    editor = Column(String(255), nullable=False)
    langue = Column(String(20), nullable=False)
    resume = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    deleted_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=False)
    id_collection = Column(Integer, ForeignKey('collection.id_collection'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    id_user_delete = Column(Integer, ForeignKey('user.id_user'))
