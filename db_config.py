from os import environ
from dotenv import load_dotenv
load_dotenv('.env')
TORTOISE_ORM = {
    "connections": {"default": environ.get('DATABASE_URL', 'None')},
    "apps": {
        "models": {
            "models": ["messages.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
print(TORTOISE_ORM)
