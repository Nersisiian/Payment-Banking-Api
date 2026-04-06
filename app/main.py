from fastapi import FastAPI, Request
import time
from app.api import auth, transactions, accounts

app = FastAPI(title="Banking API")

app.include_router(auth.router, prefix="/auth")
app.include_router(transactions.router, prefix="/transactions")
app.include_router(accounts.router, prefix="/accounts")

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url} - {duration:.3f}s")
    return response

@app.get("/")
def root():
    return {"status": "Bank API running"}