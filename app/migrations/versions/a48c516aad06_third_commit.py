"""Third commit

Revision ID: a48c516aad06
Revises: 1cc86f76f5e5
Create Date: 2024-10-05 21:38:12.686318

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a48c516aad06'
down_revision: Union[str, None] = '1cc86f76f5e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###
