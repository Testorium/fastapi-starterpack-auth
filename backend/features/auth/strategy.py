from fastapi_users.authentication.strategy.db import DatabaseStrategy
from features.auth.access_token.deps import AccessTokenDependency


def get_database_strategy(access_token_db: AccessTokenDependency) -> DatabaseStrategy:
    return DatabaseStrategy(
        access_token_db,
        lifetime_seconds=900,
    )
