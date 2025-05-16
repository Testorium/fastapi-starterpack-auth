from fastapi_users.authentication import AuthenticationBackend

from .strategy import get_database_strategy
from .transport import cookie_transport

authentication_backend = AuthenticationBackend(
    name="access-token-database",
    transport=cookie_transport,
    get_strategy=get_database_strategy,
)
