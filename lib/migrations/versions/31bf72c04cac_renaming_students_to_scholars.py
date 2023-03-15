"""Renaming students to scholars

Revision ID: 31bf72c04cac
Revises: 791279dd0760
Create Date: 2023-03-15 13:53:24.154365

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31bf72c04cac'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
