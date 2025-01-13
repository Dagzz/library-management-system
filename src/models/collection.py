# ============================================
# Table: collection
# ============================================

from sqlalchemy import Column, Integer, Text, String, UniqueConstraint
from sqlalchemy.orm import relationship
from .base import Base

class Collection(Base):
    __tablename__ = 'collection'
    __table_args__ = (
        UniqueConstraint('collection_name', name='collection_AK'),
    )

    id_collection = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    collection_name = Column(String(50), nullable=False)

    books = relationship("Book", back_populates="collection")

    def __repr__(self):
        return f"<Collection(id_collection={self.id_collection}, collection_name='{self.collection_name}')>"
