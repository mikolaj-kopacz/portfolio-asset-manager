from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
DB_FILE = BASE_DIR / "assets.db"

class Settings(BaseSettings):
    PROJECT_NAME: str = "Asset Manager"
    DATABASE_URL: str = f"sqlite:///{DB_FILE}"

settings = Settings()