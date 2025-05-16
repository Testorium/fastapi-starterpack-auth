from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyBaseAccessTokenTable
from fastapi_users_db_sqlalchemy.generics import GUID
from shared.models.base import Base
from shared.models.mixins.pk_int import INTPrimaryKeyMixin
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable, INTPrimaryKeyMixin):
    user_id: Mapped[GUID] = mapped_column(
        GUID,
        ForeignKey("users.id", ondelete="cascade"),
        nullable=False,
    )
