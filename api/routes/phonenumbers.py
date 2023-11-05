from fastapi import APIRouter, Request, Security
from typing import List
from routes.auth import get_api_key
from models.PhoneNumber import PhoneNumber
from models import DBBase



router = APIRouter()
@router.get("/")
def getAllPhoneNumbers(request: Request,api_key: str = Security(get_api_key)) ->  List[PhoneNumber]:
    return request.app.db.query(DBBase.PhoneNumber)