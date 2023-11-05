from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    sender = Column(String,index=True)
    received = Column(DateTime)
    phonenumber_id = Column(Integer, ForeignKey("phonenumbers.id"))
    phonenumber = relationship("PhoneNumber", back_populates="messages")

class PhoneNumber(Base):
    __tablename__ = "phonenumbers"

    id = Column(Integer, primary_key=True, index=True)
    phonenumber = Column(String, index=True)
    lastreceived = Column(DateTime)
    lastsent = Column(DateTime)
    messages = relationship("Message", back_populates="phonenumber")