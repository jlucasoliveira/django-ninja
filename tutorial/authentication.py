from typing import Any, Optional
import jwt
from asgiref.sync import sync_to_async
from ninja.security import HttpBearer
from django.contrib.auth import get_user_model
from tutorial import settings
from users.exceptions import InvalidCredentials


UserModel = get_user_model()


JWT_SECRET = settings.config("JWT_SECRET")


class BearerAuthentication(HttpBearer):
    async def authenticate(self, request, token: str) -> Optional[Any]:
        try:
            payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            user = await sync_to_async(UserModel.objects.get)(pk=payload['id'])
            return user
        except UserModel.DoesNotExist:
            raise InvalidCredentials()
        except:
            raise
