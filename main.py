from fastapi import FastAPI
from contextlib import asynccontextmanager
from routes.base import router as base_router
from routes.messages import router as messages_router
from routes.phonenumbers import router as phonenumbers_router

from fastapi import FastAPI
from database import SessionLocal, engine
from models.DBBase import Base

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.db = SessionLocal()
    yield
    app.db.close()

app = FastAPI(lifespan=lifespan)
app.include_router(base_router, tags=["base"], prefix="")
app.include_router(messages_router, tags=["messages"], prefix="/messages")
app.include_router(phonenumbers_router, tags=["phonenumbers"], prefix="/numbers")



