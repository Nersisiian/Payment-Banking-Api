from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import get_db
from app.models.account import Account

router = APIRouter()

@router.get("/{user_id}")
async def get_balance(user_id: int, db: AsyncSession = Depends(get_db)):
    acc = (await db.execute(
        select(Account).where(Account.user_id == user_id)
    )).scalar_one()

    return {"balance": acc.balance}