from fastapi import Depends, APIRouter
from sqlmodel import Session
from src.asset_manager.db.session import get_db
from src.asset_manager.db.models import Asset
from src.asset_manager.schemas.asset import AssetCreate, AssetRead
from src.asset_manager.db.models import User
from src.asset_manager.api.deps import get_current_user

router = APIRouter()

@router.post("/",response_model=AssetRead)
def create_asset(asset_in: AssetCreate,db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    asset = Asset(**asset_in.model_dump(),owner_id = current_user.id)
    asset.owner_id = current_user.id
    db.add(asset)
    db.commit()
    db.refresh(asset)

    return asset