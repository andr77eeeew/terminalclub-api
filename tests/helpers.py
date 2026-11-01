from typing import Protocol

from fastapi.testclient import TestClient

from terminalclub_api.core.settings import Settings


class MakeClient(Protocol):
    def __call__(self, settings: Settings | None = None) -> TestClient: ...
