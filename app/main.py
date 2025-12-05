from fastapi import FastAPI

from app.api import routes_auth, routes_coins, routes_categories, routes_health
from app.config import get_settings


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description=(
            "Technical exercise: REST API exposing cryptocurrency "
            "market data fetched from CoinGecko."
        ),
    )

    # Register routers
    app.include_router(routes_auth.router)
    app.include_router(routes_coins.router)
    app.include_router(routes_categories.router)
    app.include_router(routes_health.router)

    return app


app = create_app()
