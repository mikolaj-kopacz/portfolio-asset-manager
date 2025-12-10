from sqlmodel import SQLModel


class AssetBase(SQLModel):
    ticker: str
    amount: float


class AssetCreate(AssetBase):
    pass


class AssetRead(AssetBase):
    id: int
