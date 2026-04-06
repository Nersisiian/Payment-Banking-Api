# 💳 Payment-Banking-API

[![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)](https://www.python.org/) 
[![FastAPI](https://img.shields.io/badge/FastAPI-0.99-green?style=for-the-badge)](https://fastapi.tiangolo.com/) 
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue?style=for-the-badge)](https://www.postgresql.org/) 
[![Docker](https://img.shields.io/badge/Docker-24.0-blue?style=for-the-badge)](https://www.docker.com/) 
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

A **robust and scalable API** for handling banking and payment operations, built with **FastAPI**, **PostgreSQL**, **Celery**, and **Redis**. Designed for fintech applications requiring secure, high-performance transaction processing.

---

## 🚀 Features

- **User Management:** Create, update, and authenticate users.
- **Bank Accounts:** Support for multiple accounts per user.
- **Transactions:** Secure money transfers, deposits, and withdrawals.
- **Asynchronous Tasks:** Background processing via Celery + Redis.
- **Database Migrations:** Managed with Alembic.
- **Dockerized:** Easy deployment with Docker and Docker Compose.
- **API Documentation:** Interactive docs via Swagger UI and Redoc.

---

## 🛠 Tech Stack

- **Backend:** Python 3.11, FastAPI
- **Database:** PostgreSQL
- **Task Queue:** Celery + Redis
- **Migrations:** Alembic
- **Containerization:** Docker & Docker Compose
- **Testing:** Pytest

---

## ⚡ Getting Started

### Prerequisites

- [Python 3.11](https://www.python.org/downloads/)
- [Docker & Docker Compose](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/) (optional if using Docker)

### Installation

Clone the repository:

```bash
git clone https://github.com/Nersisiian/Payment-Banking-Api.git
cd Payment-Banking-Api

Create a .env file (example):

DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/payments
REDIS_URL=redis://redis:6379/0
SECRET_KEY=your-secret-key

Build and run the Docker containers:

docker-compose up --build
Apply Database Migrations
docker-compose exec web alembic upgrade head
📄 API Documentation
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

All endpoints are fully documented with request and response schemas.

🔧 Usage

Example: Creating a transaction

POST /transactions/
Content-Type: application/json

{
    "from_account": "12345678",
    "to_account": "87654321",
    "amount": 100.50,
    "currency": "USD"
}

Response:

{
    "id": 1,
    "from_account": "12345678",
    "to_account": "87654321",
    "amount": 100.5,
    "currency": "USD",
    "status": "processed",
    "created_at": "2026-04-06T18:00:00Z"
}
🧪 Running Tests
docker-compose exec web pytest --cov=app

🌐 Deployment

Deploy via Docker Compose or integrate with Kubernetes for production. Recommended to use environment variables for sensitive credentials.

🤝 Contributing

Contributions are welcome! Please follow these steps:

1.Fork the repository.
2.Create a new branch (git checkout -b feature/YourFeature).
3.Make your changes and commit (git commit -m 'Add feature').
4.Push to the branch (git push origin feature/YourFeature).
5.Open a Pull Request.

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

📞 Contact

Author: Nersisiian
GitHub: https://github.com/Nersisiian

Email: nersisyangrish13@gmail.com
