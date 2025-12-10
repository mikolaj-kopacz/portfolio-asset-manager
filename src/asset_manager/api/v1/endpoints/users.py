from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from src.asset_manager.db.session import get_db
from src.asset_manager.db.models import User
from src.asset_manager.schemas.user import UserCreate, UserRead
from src.asset_manager.core.security import get_password_hash

router = APIRouter()


@router.post("/", response_model=UserRead)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    if db.exec(select(User).where(User.email == user_in.email)).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        user = User(
            email=user_in.email, hashed_password=get_password_hash(user_in.password)
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
