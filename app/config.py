from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    

    app_name: str = "Vetty Crypto Market API"
    version: str = "1.0.0"

    # JWT settings
    jwt_secret_key: str = "CHANGE_ME_SUPER_SECRET"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # Demo user (for the exercise only)
    demo_username: str = "admin"
    demo_password: str = "admin123"

    # CoinGecko
    coingecko_base_url: str = "https://api.coingecko.com/api/v3"

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """Return a cached instance of settings."""
    return Settings()
