import os

from dotenv import load_dotenv

load_dotenv()


# --- Gunicorn Configuration ---
class GunicornConfig:
    host: str = "0.0.0.0"
    port: int = 8000
    timeout: int = 900
    workers: int = 1
    log_level: str = "info"


gunicorn_config = GunicornConfig()


# --- Database Configuration ---
class DatabaseConfig:
    driver: str = "postgresql+asyncpg"
    user: str | None = os.getenv("POSTGRES_USER")
    password: str | None = os.getenv("POSTGRES_PASSWORD")
    host: str | None = os.getenv("POSTGRES_HOST")
    port: str | None = os.getenv("POSTGRES_PORT")
    db_name: str | None = os.getenv("POSTGRES_DB")

    echo: bool = os.getenv("DB_ECHO", "false").lower() == "true"
    echo_pool: bool = os.getenv("DB_ECHO_POOL", "false").lower() == "true"
    pool_size: int = int(os.getenv("DB_POOL_SIZE", 10))
    max_overflow: int = int(os.getenv("DB_MAX_OVERFLOW", 100))

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }

    @property
    def dns(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"


db_config = DatabaseConfig()


# --- Cors Configuration ---
class CorsConfig:
    allow_origins: list[str] = [
        "http://localhost:3000",
    ]
    allow_credentials: bool = True
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


cors_config = CorsConfig()
