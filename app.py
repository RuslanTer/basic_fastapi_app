from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from db_config import TORTOISE_ORM
from messages.routes import router as msg_router

app = FastAPI()

app.include_router(msg_router)

register_tortoise(
    app,
    config=TORTOISE_ORM
)
