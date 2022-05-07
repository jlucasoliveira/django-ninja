from asgiref.sync import sync_to_async
from datetime import timedelta
import jwt
from django.utils import timezone
from tutorial.settings import config


JWT_SECRET = config("JWT_SECRET")

@sync_to_async
def generate_token(data: dict) -> str:
    now = timezone.now()
    payload = {
        "exp": now + timedelta(days=15),
        "iat": now,
    }

    for key, value in data.items():
        payload[key] = value

    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

    return token