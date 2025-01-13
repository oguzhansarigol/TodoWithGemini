"""phone number added

Revision ID: de5e53917260
Revises: 
Create Date: 2025-01-12 15:01:13.863356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de5e53917260'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("users",sa.Column("phone_number",sa.String(),nullable=True))


def downgrade() -> None:
    #op.drop_column("users","phone_number")
    pass
