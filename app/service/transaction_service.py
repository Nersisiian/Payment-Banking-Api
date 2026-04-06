from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.account import Account
from app.models.transaction import Transaction
from app.utils.fraud import is_suspicious
from app.utils.logger import logger

async def transfer_money(db: AsyncSession, from_user: int, to_user: int, amount: float, idem_key: str):

    if amount <= 0:
        raise HTTPException(status_code=400, detail="Invalid amount")

    if from_user == to_user:
        raise HTTPException(status_code=400, detail="Cannot send to yourself")

    existing = (await db.execute(
        select(Transaction).where(Transaction.idempotency_key == idem_key)
    )).scalar_one_or_none()

    if existing:
        return existing

    sender = (await db.execute(
        select(Account).where(Account.user_id == from_user)
    )).scalar_one()

    receiver = (await db.execute(
        select(Account).where(Account.user_id == to_user)
    )).scalar_one()

    if sender.balance < amount:
        raise HTTPException(status_code=400, detail="Insufficient funds")

    status = "flagged" if is_suspicious(amount) else "success"

    async with db.begin():
        sender.balance -= amount
        receiver.balance += amount

        tx = Transaction(
            from_user=from_user,
            to_user=to_user,
            amount=amount,
            status=status,
            idempotency_key=idem_key
        )

        db.add(tx)

    logger.info(f"Transfer {from_user} -> {to_user} | {amount}")

    return tx