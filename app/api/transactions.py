from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.schemas.transaction import TransferRequest
from app.services.transaction_service import transfer_money
from app.utils.rate_limiter import is_allowed

router = APIRouter()

@router.post("/transfer")
async def transfer(data: TransferRequest, db: AsyncSession = Depends(get_db)):

    if not is_allowed(f"user:{data.from_user}"):
        raise HTTPException(status_code=429, detail="Too many requests")

    tx = await transfer_money(
        db,
        data.from_user,
        data.to_user,
        data.amount,
        data.idempotency_key
    )

    return {
        "transaction_id": tx.id,
        "status": tx.status,
        "amount": tx.amount
    }