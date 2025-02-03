"""empty message

Revision ID: 57446be35033
Revises: dbbff74108b4
Create Date: 2025-02-03 19:15:18.014532

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57446be35033'
down_revision = 'dbbff74108b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('diametro', sa.String(length=100), nullable=False),
    sa.Column('tiempo_rotacion', sa.String(length=100), nullable=False),
    sa.Column('tiempo_orbitacion', sa.String(length=100), nullable=False),
    sa.Column('gravedad', sa.String(length=100), nullable=False),
    sa.Column('poblacion', sa.String(length=100), nullable=False),
    sa.Column('clima', sa.String(length=100), nullable=False),
    sa.Column('terreno', sa.String(length=100), nullable=False),
    sa.Column('superficie_acuosa', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.Column('modelo', sa.String(length=100), nullable=False),
    sa.Column('clase_vehiculo', sa.String(length=100), nullable=False),
    sa.Column('fabricante', sa.String(length=100), nullable=False),
    sa.Column('longitud', sa.String(length=100), nullable=False),
    sa.Column('precio', sa.String(length=100), nullable=False),
    sa.Column('tripulacion', sa.String(length=100), nullable=False),
    sa.Column('velocidad_max', sa.String(length=100), nullable=False),
    sa.Column('capacidad_carga', sa.String(length=100), nullable=False),
    sa.Column('consumibles', sa.String(length=100), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Planetas')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Planetas',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('diametro', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('tiempo_rotacion', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('tiempo_orbitacion', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('gravedad', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('poblacion', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('clima', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('terreno', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('superficie_acuosa', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Planetas_pkey')
    )
    op.drop_table('vehiculos')
    op.drop_table('planetas')
    # ### end Alembic commands ###
