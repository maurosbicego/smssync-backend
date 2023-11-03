# Class Information
# A "Message" is a message element (great naming right!!) that contains details such as content, sender, when received etc.

from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
from bson.objectid import ObjectId
from datetime import datetime

from models.PhoneNumber import PhoneNumber


class Message(BaseModel):
    id: int
    content: str
    received: datetime
    sender: str
    phonenumber: int
    class Config:
        orm_mode = True

class InsertMessage(BaseModel):
    content: str
    received: datetime
    sender: str
    phonenumber: int

class GetMessage(BaseModel):
    id: int
    content: str
    received: datetime
    sender: str
    phonenumber: PhoneNumber

    class Config:
        orm_mode = True


class AddMessage(BaseModel):
    content: str
    received: datetime
    sender: str
    phonenumber: str

class DeleteMessage(BaseModel):
    id: int