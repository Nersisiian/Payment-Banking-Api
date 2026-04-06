from sqlalchemy import Column, Integer, Float, String
from app.db.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    from_user = Column(Integer)
    to_user = Column(Integer)
    amount = Column(Float)
    status = Column(String)
    idempotency_key = Column(String, unique=True)