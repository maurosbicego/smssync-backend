# Class information
# A "phoneNumber" contains the details to a specific phonnenumber. It also contains other details such as when the last SMS was sent - this is relevant to keep the prepaid contract active (provider might require usage of paid service every 6 months for example.)
from pydantic import BaseModel
from datetime import datetime

class PhoneNumber(BaseModel):
    id: int
    phonenumber: str
    lastreceived: datetime
    lastsent: datetime

class CreatePhoneNumber(BaseModel):
    phonenumber: str
    lastreceived: datetime
    lastsent: datetime
