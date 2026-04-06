from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_db
from app.models.user import User
from app.models.account import Account
from app.schemas.user import UserCreate
from app.core.security import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    await db.flush()

    account = Account(user_id=new_user.id, balance=0)
    db.add(account)

    await db.commit()

    return {"msg": "User created"}

@router.post("/login")
async def login(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    db_user = result.scalar_one_or_none()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": db_user.email})
    return {"access_token": token}