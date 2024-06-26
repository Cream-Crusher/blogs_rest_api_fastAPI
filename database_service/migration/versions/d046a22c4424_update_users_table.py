"""Update Users table

Revision ID: d046a22c4424
Revises: fbde0a70cbcc
Create Date: 2024-06-17 20:11:34.721176

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd046a22c4424'
down_revision: Union[str, None] = 'fbde0a70cbcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('fullname', sa.String(), nullable=False))
    op.add_column('users', sa.Column('phone', sa.String(), nullable=False))
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.add_column('users', sa.Column('is_superuser', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_superuser')
    op.drop_column('users', 'email')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'fullname')
    # ### end Alembic commands ###
