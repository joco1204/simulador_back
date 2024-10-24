"""Create tables

Revision ID: bbb508f4c4c3
Revises: 9ccbd76ce2d6
Create Date: 2024-10-21 13:23:31.997189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbb508f4c4c3'
down_revision = '9ccbd76ce2d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('credito',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('id_tipo_credito', sa.Integer(), nullable=False),
    sa.Column('id_linea_moto', sa.Integer(), nullable=True),
    sa.Column('valor_solicitud', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('valor_interes', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('valor_cuota', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('valor_total', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.ForeignKeyConstraint(['id_cliente'], ['clientes.id'], ),
    sa.ForeignKeyConstraint(['id_tipo_credito'], ['tipo_credito.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('credito')
    # ### end Alembic commands ###
