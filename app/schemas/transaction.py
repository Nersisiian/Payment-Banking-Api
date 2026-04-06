from pydantic import BaseModel

class TransferRequest(BaseModel):
    from_user: int
    to_user: int
    amount: float
    idempotency_key: str