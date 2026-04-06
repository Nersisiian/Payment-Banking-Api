from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import asyncio
import os
from app.db.database import Base
from app.models.user import User
from app.models.account import Account
from app.models.transaction import Transaction
from app.core.config import settings

config = context.config

fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_online():
    from sqlalchemy.ext.asyncio import create_async_engine

    connectable = create_async_engine(settings.DATABASE_URL)

    async def do_run_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(do_migrations)

    asyncio.run(do_run_migrations())

def do_migrations(connection):
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

run_migrations_online()