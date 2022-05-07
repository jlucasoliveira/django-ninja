from ninja import NinjaAPI


class InvalidCredentials(Exception):
    pass


def expired_token(instance: NinjaAPI):
    def inner(request, exc):
        return instance.create_response(
            request,
            {"detail": "JWT Token expired"},
            status=401,
        )

    return inner


def invalid_token(instance: NinjaAPI):
    def inner(request, exc):
        return instance.create_response(
            request,
            {"detail": "Invalid token signature"},
            status=401,
        )

    return inner


def user_not_found(instance: NinjaAPI):
    def inner(request, exc):
        return instance.create_response(
            request,
            {"detail": "Invalid credentials"},
            status=401,
        )

    return inner
