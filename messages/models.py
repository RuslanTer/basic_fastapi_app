from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Messages(models.Model):
    """
    Сообщения
    """

    id = fields.IntField(pk=True)
    phone = fields.CharField(max_length=25)
    email = fields.CharField(max_length=100)
    message = fields.TextField(null=True)


Messages_pd = pydantic_model_creator(Messages, name="Messages")
