from typing import List
from fastapi import APIRouter
from .models import Cars, Cars_pd

router = APIRouter(
    prefix="/car",
    tags=["MESSAGES-API"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Cars_pd])
async def get_car(model: str = "all", mark: str = "all"):
    if model == "all":
        return await Cars_pd.from_queryset(Cars.all())
    if mark != "all":
        return await Cars_pd.from_queryset(Cars.filter(model=model, mark=mark))
    return await Cars_pd.from_queryset(Cars.filter(model=model))


@router.post("/")
async def create_car(car: Cars_pd):
    car_obj = await Cars.create(**car.dict(exclude_unset=True))
    return await Cars_pd.from_tortoise_orm(car_obj)


@router.put("/")
async def update_car(car: Cars_pd):
    car_obj = Cars.filter(id=car.id)
    update_data = car.dict()
    update_data.pop("id")
    await car_obj.update(**update_data)
    return update_data


@router.delete("/delete/{pk}")
async def delete_car(pk: int):
    car_obj = await Cars.get(id=pk)
    res = await car_obj.delete()
    return res
