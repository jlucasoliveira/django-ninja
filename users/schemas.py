from django.contrib.auth import get_user_model
from ninja import Schema, ModelSchema


UserModel = get_user_model()


class UserSchema(ModelSchema):
    class Config:
        model = UserModel
        model_fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_staff",
        ]


class LoginPayload(Schema):
    username: str
    password: str


class UserResponse(Schema):
    user: UserSchema
    token: str


class RegisterPayload(Schema):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
