from pydantic_settings import BaseSettings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DB_FILE = BASE_DIR / "assets.db"


class Settings(BaseSettings):
    PROJECT_NAME: str = "Asset Manager"
    DATABASE_URL: str = f"sqlite:///{DB_FILE}"
    SECRET_KEY: str = "supersecretkey123"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
