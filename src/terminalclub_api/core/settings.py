from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TERMINALCLUB_",
        extra="ignore",
    )

    docs_enabled: bool = False
