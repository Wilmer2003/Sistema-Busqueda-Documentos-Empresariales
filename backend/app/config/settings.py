from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

RAIZ = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    elasticsearch_url: str = "http://localhost:9200"
    elasticsearch_index: str = "documentos_empresariales"
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    cors_origins: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=RAIZ / ".env", extra="ignore")


settings = Settings()