"""empty message

Revision ID: f130a90efd0f
Revises: 8216a38f2501
Create Date: 2024-11-29 13:24:27.946059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f130a90efd0f'
down_revision: Union[str, None] = '8216a38f2501'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('placemarks', sa.Column('is_active', sa.Boolean(), nullable=False, server_default="true"))
    op.alter_column('placemarks', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('placemarks', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('placemarks', 'is_active')
    # ### end Alembic commands ###
