import pytest
from helpers import MakeClient

from terminalclub_api.core.settings import Settings


@pytest.mark.parametrize("docs_enabled", [True, False])
def test_health_returns_ok(make_client: MakeClient, docs_enabled: bool) -> None:
    client = make_client(Settings(docs_enabled=docs_enabled))
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
