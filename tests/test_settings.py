from pathlib import Path

import pytest
from pydantic import ValidationError

from terminalclub_api.core.settings import Settings

ENV_VAR = "TERMINALCLUB_DOCS_ENABLED"


def test_docs_disabled_by_default(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv(ENV_VAR, raising=False)

    settings = Settings(_env_file=None)

    assert settings.docs_enabled is False


def test_docs_enabled_read_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(ENV_VAR, "true")

    settings = Settings(_env_file=None)

    assert settings.docs_enabled is True


def test_invalid_docs_enabled_raises(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(ENV_VAR, "banana")

    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_settings_read_from_env(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv(ENV_VAR, raising=False)
    (tmp_path / ".env").write_text(f"{ENV_VAR}=true\nFOO=bar\n")

    settings = Settings()

    assert settings.docs_enabled is True
