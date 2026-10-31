from fastapi import FastAPI

from terminalclub_api.health.router import router as health_router


def create_app() -> FastAPI:

    app = FastAPI(title="TerminalClub API")
    app.include_router(health_router)
    return app
