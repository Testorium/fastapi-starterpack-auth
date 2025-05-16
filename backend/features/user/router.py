from fastapi import APIRouter
from features.auth.fastapi_users import fastapi_users
from shared.config import api_prefix_config

from .schemas import UserRead, UserUpdate

router = APIRouter(prefix=api_prefix_config.v1.users, tags=["User"])

# /me
# /{id}
router.include_router(router=fastapi_users.get_users_router(UserRead, UserUpdate))
