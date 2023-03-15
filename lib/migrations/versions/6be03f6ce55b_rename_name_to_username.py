"""Rename name to username

Revision ID: 6be03f6ce55b
Revises: 31bf72c04cac
Create Date: 2023-03-15 14:04:34.368572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6be03f6ce55b'
down_revision = '31bf72c04cac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column("scholars", "name", new_column_name="username")


def downgrade() -> None:
    op.alter_column("scholars", "username", new_column_name="name")
