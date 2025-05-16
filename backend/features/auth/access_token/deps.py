from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication.strategy.db import AccessTokenDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from features.auth.access_token.model import AccessToken
from shared.database.manager import db_manager

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_access_token_db(
    session: Annotated["AsyncSession", Depends(db_manager.get_session)],
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


AccessTokenDependency = Annotated[
    AccessTokenDatabase[AccessToken], Depends(get_access_token_db)
]
