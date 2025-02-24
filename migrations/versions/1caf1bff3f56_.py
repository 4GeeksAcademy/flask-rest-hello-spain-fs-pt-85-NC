"""empty message

Revision ID: 1caf1bff3f56
Revises: 0055319ed34f
Create Date: 2025-02-04 20:51:30.365020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1caf1bff3f56'
down_revision = '0055319ed34f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)

    # ### end Alembic commands ###
