from pathlib import Path

import pytest
from helpers import MakeClient

from terminalclub_api.core.settings import Settings

DOCS_PATHS = ["/docs", "/redoc", "/openapi.json"]

ENV_VAR = "TERMINALCLUB_DOCS_ENABLED"


@pytest.mark.parametrize("path", DOCS_PATHS)
def test_docs_disabled_returns_404(make_client: MakeClient, path: str) -> None:
    client = make_client(Settings(docs_enabled=False))

    assert client.get(path).status_code == 404


@pytest.mark.parametrize("path", DOCS_PATHS)
def test_docs_enabled_returns_200(make_client: MakeClient, path: str) -> None:
    client = make_client(Settings(docs_enabled=True))

    assert client.get(path).status_code == 200


@pytest.mark.parametrize(
    ("env_value", "expected_status"),
    [
        ("true", 200),
        ("false", 404),
    ],
)
def test_create_app_reads_docs_enabled_from_env(
    make_client: MakeClient,
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    env_value: str,
    expected_status: int,
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv(ENV_VAR, env_value)

    client = make_client()

    assert client.get("/docs").status_code == expected_status
