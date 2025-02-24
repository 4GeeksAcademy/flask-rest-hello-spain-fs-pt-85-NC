"""empty message

Revision ID: e8047bfc77aa
Revises: a028b4ad72e1
Create Date: 2025-02-04 22:20:25.092181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8047bfc77aa'
down_revision = 'a028b4ad72e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personajes_favoritos',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('personaje_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['personaje_id'], ['personajes.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'personaje_id')
    )
    op.create_table('planetas_favoritos',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planeta_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planeta_id'], ['planetas.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'planeta_id')
    )
    op.create_table('vehiculos_favoritos',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vehiculo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehiculo_id'], ['vehiculos.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'vehiculo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehiculos_favoritos')
    op.drop_table('planetas_favoritos')
    op.drop_table('personajes_favoritos')
    # ### end Alembic commands ###
