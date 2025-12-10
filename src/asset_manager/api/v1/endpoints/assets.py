from fastapi import Depends, APIRouter
from sqlmodel import Session
from src.asset_manager.db.session import get_db
from src.asset_manager.db.models import Asset
from src.asset_manager.schemas.asset import AssetCreate, AssetRead
from src.asset_manager.db.models import User
from src.asset_manager.api.deps import get_current_user
from typing import List
from sqlmodel import select

router = APIRouter()


@router.post("/", response_model=AssetRead)
def create_asset(
    asset_in: AssetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    asset = Asset(**asset_in.model_dump(), owner_id=current_user.id)
    db.add(asset)
    db.commit()
    db.refresh(asset)

    return asset


@router.get("/", response_model=List[AssetRead])
def read_assets(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    assets = db.exec(select(Asset).where(Asset.owner_id == current_user.id)).all()
    return assets
