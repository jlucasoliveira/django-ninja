from asgiref.sync import sync_to_async
from ninja.router import Router
from django.contrib.auth import authenticate, get_user_model
from users import schemas, utils, exceptions


UserModel = get_user_model()
router = Router(tags=["Users"])


@router.post("/login", auth=None, response=schemas.UserResponse)
async def login(request, payload: schemas.LoginPayload):
    user = await sync_to_async(authenticate)(**payload.dict())

    if not user:
        raise exceptions.InvalidCredentials()

    token_payload = {"id": user.id}
    token = await utils.generate_token(token_payload)

    response_data = {
        "user": user,
        "token": token,
    }

    return response_data


@router.post("/register", auth=None, response=schemas.UserResponse)
async def register(request, payload: schemas.RegisterPayload):
    user = await sync_to_async(UserModel.objects.create)(**payload.dict(), is_staff=False)

    token_payload = {"id": user.id}
    token = await utils.generate_token(token_payload)

    response_data = {
        "user": user,
        "token": token,
    }
    return response_data


@router.get("/me", response=schemas.UserSchema)
async def me(request):
    return await request.auth