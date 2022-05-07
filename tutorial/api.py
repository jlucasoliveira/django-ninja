import jwt
from ninja import NinjaAPI
from tutorial.authentication import BearerAuthentication
from tutorial.parsers import JSONParser, JSONRenderer
from polls.views import router as polls_router
from users.views import router as auth_router
from users import exceptions


def get_application() -> NinjaAPI:
    app: NinjaAPI = NinjaAPI(
        title="Ninja API",
        description="Django Ninja Learning API docs",
        auth=BearerAuthentication(),
        parser=JSONParser(),
        renderer=JSONRenderer(),
    )

    app.add_router("/polls", polls_router)
    app.add_router("/auth", auth_router)

    app.add_exception_handler(jwt.ExpiredSignatureError, exceptions.expired_token(app))
    app.add_exception_handler(jwt.InvalidSignatureError, exceptions.invalid_token(app))
    app.add_exception_handler(exceptions.InvalidCredentials, exceptions.user_not_found(app))

    return app


app: NinjaAPI = get_application()
