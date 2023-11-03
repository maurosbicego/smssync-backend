from fastapi import APIRouter, Request, Security
from typing import List
from routes.auth import get_api_key


router = APIRouter()
@router.get("/")
def base(request: Request,api_key: str = Security(get_api_key)):
    return {"msg": "API for SMSSync"}   