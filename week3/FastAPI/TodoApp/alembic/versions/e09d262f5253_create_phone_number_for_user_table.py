"""Create phone number for user table

Revision ID: e09d262f5253
Revises: 
Create Date: 2026-04-27 07:36:38.319651

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e09d262f5253'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# alembic upgrade <revision_id>
def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(),nullable=True))

# alembic downgrade <revision_id>
def downgrade() -> None:
    op.drop_column('users','phone_number')
