from sqlmodel import SQLModel

class UserBase(SQLModel):
    email: str

class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    is_active: bool
