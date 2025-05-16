from fastapi import APIRouter
from shared.config import api_prefix_config

from .v1 import router as v1_router

router = APIRouter(prefix=api_prefix_config.prefix)

router.include_router(v1_router)
