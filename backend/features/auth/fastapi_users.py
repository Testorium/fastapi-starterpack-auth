import uuid

from fastapi_users import FastAPIUsers
from features.user.deps import get_user_manager
from features.user.model import User

from .backend import authentication_backend

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [authentication_backend],
)
