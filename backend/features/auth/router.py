from fastapi import APIRouter, Depends
from features.user.schemas import UserCreate, UserRead
from shared.config import api_prefix_config

from .backend import authentication_backend
from .fastapi_users import fastapi_users

router = APIRouter(prefix=api_prefix_config.v1.auth, tags=["Auth"])

# /login
# /logout
router.include_router(router=fastapi_users.get_auth_router(authentication_backend))

# /register
router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
    # dependencies=[Depends(fastapi_users.current_user(active=True, superuser=True))],
)

# /request-verify-token
# /verify
# router.include_router(router=fastapi_users.get_verify_router(UserRead))


# /forgot-password
# /reset-password
router.include_router(router=fastapi_users.get_reset_password_router())
