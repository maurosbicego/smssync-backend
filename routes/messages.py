from fastapi import APIRouter, Request, HTTPException, status, Security
from fastapi.encoders import jsonable_encoder
from typing import List
from routes.auth import get_api_key
from models.Message import GetMessage, AddMessage
from models import DBBase
import datetime
from config import config
from sqlalchemy import func

def deleteOldMessages(db):
    timedelta = datetime.datetime.now() - datetime.timedelta(hours=config["deleteMessagesAfterHours"])
    db.query(DBBase.Message).filter(func.DATETIME(DBBase.Message.received) < timedelta).delete()


router = APIRouter()
@router.get("/")
def getAllMessages(request: Request,api_key: str = Security(get_api_key)) ->  List[GetMessage]:
    deleteOldMessages(request.app.db)
    return request.app.db.query(DBBase.Message)

@router.post("/")
def addMessage(request: Request, message: AddMessage, api_key: str = Security(get_api_key)) ->  GetMessage:
    if request.app.db.query(DBBase.Message).filter(DBBase.Message.content == message.content, DBBase.Message.sender == message.sender, DBBase.Message.received == message.received).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Message already exists")
    phonenumber = request.app.db.query(DBBase.PhoneNumber).filter(DBBase.PhoneNumber.phonenumber == message.phonenumber).first()
    if not phonenumber:
        phoneObj = DBBase.PhoneNumber(phonenumber=message.phonenumber,lastreceived=message.received,lastsent=message.received)
        request.app.db.add(phoneObj)
        request.app.db.commit()
        request.app.db.refresh(phoneObj)
        phonenumber = request.app.db.query(DBBase.PhoneNumber).filter(DBBase.PhoneNumber.phonenumber == message.phonenumber).first()

    msgObj = DBBase.Message(content=message.content,received=message.received,sender=message.sender,phonenumber_id=phonenumber.id)
    request.app.db.add(msgObj)
    request.app.db.commit()
    request.app.db.refresh(msgObj)

    inserted = request.app.db.query(DBBase.Message).filter(DBBase.Message.content == message.content, DBBase.Message.sender == message.sender, DBBase.Message.received == message.received).first()
    inserted.phonenumber = inserted.phonenumber # load ORM data
    deleteOldMessages(request.app.db)
    return jsonable_encoder(inserted)