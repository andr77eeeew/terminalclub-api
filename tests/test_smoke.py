import importlib


def test_package() -> None:
    importlib.import_module("terminalclub_api")
