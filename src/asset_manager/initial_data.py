from sqlmodel import SQLModel
from src.asset_manager.db.session import engine


def init_db():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
