"""Nullear columnas en control diario

Revision ID: 9ebac80edbb0
Revises: 563a4af62d31
Create Date: 2024-09-12 16:38:45.759447

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9ebac80edbb0'
down_revision = '563a4af62d31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('control_diario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('id_matafuego', sa.Integer(), nullable=True))
        batch_op.alter_column('id_elemento',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.drop_constraint('control_diario_ibfk_3', type_='foreignkey')
        batch_op.create_foreign_key(None, 'matafuegos', ['id_matafuego'], ['id_matafuego'])
        batch_op.drop_column('matafuegos_id_matafuego')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('control_diario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('matafuegos_id_matafuego', mysql.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('control_diario_ibfk_3', 'matafuegos', ['matafuegos_id_matafuego'], ['id_matafuego'])
        batch_op.alter_column('id_elemento',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.drop_column('id_matafuego')

    # ### end Alembic commands ###
