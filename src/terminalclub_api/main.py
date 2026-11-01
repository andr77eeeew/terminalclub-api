from fastapi import FastAPI

from terminalclub_api.core.settings import Settings
from terminalclub_api.health.router import router as health_router


def create_app(settings: Settings | None = None) -> FastAPI:
    if settings is None:
        settings = Settings()
    app = FastAPI(
        title="TerminalClub API",
        openapi_url="/openapi.json" if settings.docs_enabled else None,
    )
    app.include_router(health_router)
    return app
