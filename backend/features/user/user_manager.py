import uuid
from typing import TYPE_CHECKING

from fastapi_users import BaseUserManager, UUIDIDMixin
from shared.config import access_token_config

from .model import User

if TYPE_CHECKING:
    from fastapi import Request


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = access_token_config.reset_password_token_secret
    verification_token_secret = access_token_config.verification_token_secret

    async def on_after_register(
        self,
        user: User,
        request: "Request | None",
    ):
        pass

    async def on_after_forgot_password(
        self,
        user: User,
        token: str,
        request: "Request | None",
    ):
        pass

    async def on_after_request_verify(
        self,
        user: User,
        token: str,
        request: "Request | None",
    ):
        pass
