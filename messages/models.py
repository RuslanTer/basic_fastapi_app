from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Cars(models.Model):
    """
    Модель автомобиля
    """

    id = fields.IntField(pk=True)
    model = fields.CharField(max_length=25)
    mark = fields.CharField(max_length=100)
    price = fields.TextField(null=True)


Cars_pd = pydantic_model_creator(Cars, name="Cars")
