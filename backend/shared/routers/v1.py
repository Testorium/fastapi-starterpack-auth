from fastapi import APIRouter
from features.auth.router import router as auth_router
from features.user.router import router as user_router
from shared.config import api_prefix_config

router = APIRouter(prefix=api_prefix_config.v1.prefix)

router.include_router(auth_router)
router.include_router(user_router)
