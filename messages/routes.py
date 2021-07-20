from typing import List
from fastapi import APIRouter
from .models import Messages, Messages_pd


router = APIRouter(
    prefix="/msg",
    tags=["MESSAGES-API"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{email}", response_model=List[Messages_pd])
async def select_base_route(email: str):
    return await Messages_pd.from_queryset(Messages.filter(email=email))


@router.post("/send/")
async def select_base_route(message: Messages_pd):
    msg_obj = await Messages.create(**message.dict(exclude_unset=True))
    return await Messages_pd.from_tortoise_orm(msg_obj)
