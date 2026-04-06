"""init

Revision ID: 20260406_01
Revises: 
Create Date: 2026-04-06 20:00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20260406_01'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, unique=True),
        sa.Column('password', sa.String),
    )

    op.create_table(
        'accounts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('balance', sa.Float, default=0)
    )

    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('from_user', sa.Integer),
        sa.Column('to_user', sa.Integer),
        sa.Column('amount', sa.Float),
        sa.Column('status', sa.String),
        sa.Column('idempotency_key', sa.String, unique=True)
    )

def downgrade():
    op.drop_table('transactions')
    op.drop_table('accounts')
    op.drop_table('users')