from sqlalchemy import Column, Integer, Text, Date, Enum, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Notification(Base):
    __tablename__ = 'notification'

    id_notification = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(Text, nullable=False)
    notification_date = Column(Date, nullable=False)
    notification_type = Column(Enum('rappel', 'retard', 'confirmation'), nullable=False)
    seen = Column(Boolean, nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
