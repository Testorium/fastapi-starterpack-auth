from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from shared.database.manager import db_manager

from .model import User
from .user_manager import UserManager

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated["AsyncSession", Depends(db_manager.get_session)],
):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(
    user_db: Annotated[SQLAlchemyUserDatabase, Depends(get_user_db)],
):
    yield UserManager(user_db)
