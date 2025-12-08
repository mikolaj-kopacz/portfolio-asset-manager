from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./assets.db"
    PROJECT_NAME: str  = "Asset Manager"


settings = Settings()