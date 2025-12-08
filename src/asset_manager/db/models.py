from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    hashed_password: str = Field()
    is_active: bool = Field(default=True)

    assets: List["Asset"] = Relationship(back_populates="owner")

class Asset(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    ticker: str = Field()
    amount: float = Field()
    owner_id: int = Field(foreign_key="user.id")

    owner: Optional[User] = Relationship(back_populates="assets")