"""Create tables

Revision ID: 9ccbd76ce2d6
Revises: e9e5f92c5494
Create Date: 2024-10-21 10:12:09.277788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ccbd76ce2d6'
down_revision = 'e9e5f92c5494'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clientes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_tipo_documento', sa.Integer(), nullable=False),
    sa.Column('numero_documento', sa.String(length=12), nullable=False),
    sa.Column('nombres', sa.String(length=255), nullable=False),
    sa.Column('apellidos', sa.String(length=255), nullable=False),
    sa.Column('celular', sa.String(length=10), nullable=False),
    sa.Column('direccion', sa.String(length=100), nullable=True),
    sa.Column('barrio', sa.String(length=100), nullable=True),
    sa.Column('ciudad', sa.String(length=50), nullable=True),
    sa.Column('departamento', sa.String(length=50), nullable=True),
    sa.Column('nombre_referencia_1', sa.String(length=100), nullable=True),
    sa.Column('celular_referencia_1', sa.String(length=10), nullable=True),
    sa.Column('nombre_referencia_2', sa.String(length=100), nullable=True),
    sa.Column('celular_referencia_2', sa.String(length=10), nullable=True),
    sa.ForeignKeyConstraint(['id_tipo_documento'], ['tipo_documento.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clientes')
    # ### end Alembic commands ###
