from collections.abc import Iterator
from contextlib import ExitStack

import pytest
from fastapi.testclient import TestClient
from helpers import MakeClient

from terminalclub_api.core.settings import Settings
from terminalclub_api.main import create_app


@pytest.fixture
def make_client() -> Iterator[MakeClient]:
    with ExitStack() as stack:

        def _make_client(settings: Settings | None = None) -> TestClient:
            return stack.enter_context(TestClient(create_app(settings)))

        yield _make_client
