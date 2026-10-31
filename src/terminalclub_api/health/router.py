from fastapi import APIRouter

from terminalclub_api.health.schemas import HealthResponse

router = APIRouter(tags=["Health"])


@router.get("/health")
def health() -> HealthResponse:
    return HealthResponse(status="ok")
