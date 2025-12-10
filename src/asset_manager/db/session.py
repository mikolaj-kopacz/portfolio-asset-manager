from sqlmodel import create_engine
from src.asset_manager.core.config import settings

engine = create_engine(
    settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)


def get_db():
    from sqlmodel import Session

    with Session(engine) as session:
        yield session
