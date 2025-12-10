from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError
from sqlmodel import Session, select
from src.asset_manager.db.session import get_db
from src.asset_manager.db.models import User
from src.asset_manager.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)],db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})

    try:
        payload = jwt.decode(token,settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    user = db.exec(select(User).where(User.email == email)).first()

    if not user:
        raise credentials_exception

    return user