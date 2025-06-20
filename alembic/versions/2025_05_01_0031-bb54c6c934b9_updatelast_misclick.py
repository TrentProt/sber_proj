"""updatelast|misclick

Revision ID: bb54c6c934b9
Revises: 5a2cfc96ebc8
Create Date: 2025-05-01 00:31:14.440982

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb54c6c934b9'
down_revision: Union[str, None] = '5a2cfc96ebc8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('section_topic', sa.Column('img_url', sa.String(length=255), nullable=True))
    op.drop_column('topics', 'img_url')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('topics', sa.Column('img_url', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('section_topic', 'img_url')
    # ### end Alembic commands ###
