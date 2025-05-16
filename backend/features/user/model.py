from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from shared.models.base import Base
from sqlalchemy.orm import Mapped


class User(Base, SQLAlchemyBaseUserTableUUID):
    # id
    # email
    # hashed_password
    # is_active
    # is_superuser
    # is_verified
    first_name: Mapped[str]
    last_name: Mapped[str]
