"""Renaming students to scholars

Revision ID: 0c6b2b549270
Revises: 791279dd0760
Create Date: 2024-01-03 14:19:31.132549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c6b2b549270'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    pass
    op.rename_table('scholars', 'students')

