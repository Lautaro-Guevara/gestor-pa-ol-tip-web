"""Segundo intento de crear la estructura de la base de datos

Revision ID: bcdc470b412a
Revises: 
Create Date: 2024-09-10 12:30:03.885066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcdc470b412a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('area',
    sa.Column('id_area', sa.Integer(), nullable=False),
    sa.Column('nombre_area', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id_area')
    )
    op.create_table('categorias_inventario',
    sa.Column('id_categorias_inventario', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id_categorias_inventario')
    )
    op.create_table('matafuegos',
    sa.Column('id_matafuego', sa.Integer(), nullable=False),
    sa.Column('fecha_ingreso', sa.Date(), nullable=True),
    sa.Column('capacidad_matafuego', sa.Enum('1 kg', '2.5 kg', '5 kg', '10 kg'), nullable=False),
    sa.Column('fecha_vencimiento', sa.Date(), nullable=False),
    sa.Column('fecha_vencimiento_prueba_hidraulica', sa.Date(), nullable=False),
    sa.Column('ubicacion_actual_matafuego', sa.String(length=100), nullable=True),
    sa.Column('ubicacion_anterior_matafuego', sa.String(length=100), nullable=True),
    sa.Column('fecha_ultimo_movimiento', sa.Date(), nullable=True),
    sa.Column('despresurizado', sa.String(length=45), nullable=True),
    sa.Column('matafuegoscol', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_matafuego')
    )
    op.create_table('matafuegos_recarga',
    sa.Column('id_matafuegos_recarga', sa.Integer(), nullable=False),
    sa.Column('fecha_enviado', sa.Date(), nullable=False),
    sa.Column('fecha_recibido', sa.Date(), nullable=False),
    sa.Column('activo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id_matafuegos_recarga')
    )
    op.create_table('tipo_vestimenta_epp',
    sa.Column('id_tipo_vestimenta_epp', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('descripcion', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id_tipo_vestimenta_epp'),
    sa.UniqueConstraint('descripcion')
    )
    op.create_table('elementos',
    sa.Column('id_elementos', sa.Integer(), nullable=False),
    sa.Column('id_categorias_inventario', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['id_categorias_inventario'], ['categorias_inventario.id_categorias_inventario'], ),
    sa.PrimaryKeyConstraint('id_elementos')
    )
    op.create_table('sector',
    sa.Column('id_sector', sa.Integer(), nullable=False),
    sa.Column('nombre_sector', sa.String(length=45), nullable=False),
    sa.Column('area_id_area', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['area_id_area'], ['area.id_area'], ),
    sa.PrimaryKeyConstraint('id_sector')
    )
    op.create_table('talles_epp',
    sa.Column('id_talles_epp', sa.Integer(), nullable=False),
    sa.Column('talle', sa.String(length=45), nullable=False),
    sa.Column('genero', sa.Enum('Hombre', 'Mujer', 'Unisex'), nullable=False),
    sa.Column('tipo_vestimenta_epp_id_tipo_vestimenta_epp', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['tipo_vestimenta_epp_id_tipo_vestimenta_epp'], ['tipo_vestimenta_epp.id_tipo_vestimenta_epp'], ),
    sa.PrimaryKeyConstraint('id_talles_epp')
    )
    op.create_table('personal',
    sa.Column('legajo_personal', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=45), nullable=False),
    sa.Column('apellido', sa.String(length=45), nullable=False),
    sa.Column('sector_id_sector', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['sector_id_sector'], ['sector.id_sector'], ),
    sa.PrimaryKeyConstraint('legajo_personal')
    )
    op.create_table('stock',
    sa.Column('id_stock', sa.Integer(), nullable=False),
    sa.Column('id_elemento', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('imputacion', sa.String(length=45), nullable=True),
    sa.ForeignKeyConstraint(['id_elemento'], ['elementos.id_elementos'], ),
    sa.PrimaryKeyConstraint('id_stock')
    )
    op.create_table('control_diario',
    sa.Column('id_control_diario', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('id_elemento', sa.Integer(), nullable=False),
    sa.Column('legajo_personal', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('comentarios', sa.String(length=45), nullable=True),
    sa.Column('matafuegos_id_matafuego', sa.Integer(), nullable=False),
    sa.Column('accion', sa.Enum('Retiro', 'Prestamo', 'Dejo', 'Devolvio', 'Intercambio', 'A Cargo'), nullable=False),
    sa.ForeignKeyConstraint(['id_elemento'], ['elementos.id_elementos'], ),
    sa.ForeignKeyConstraint(['legajo_personal'], ['personal.legajo_personal'], ),
    sa.ForeignKeyConstraint(['matafuegos_id_matafuego'], ['matafuegos.id_matafuego'], ),
    sa.PrimaryKeyConstraint('id_control_diario')
    )
    op.create_table('elementos_numerados',
    sa.Column('id_numeracion_elementos', sa.Integer(), nullable=False),
    sa.Column('legajo_personal', sa.Integer(), nullable=False),
    sa.Column('fecha_recepcion', sa.Date(), nullable=True),
    sa.Column('categoria', sa.String(length=45), nullable=False),
    sa.Column('nombre_elemento', sa.String(length=45), nullable=False),
    sa.Column('marca_elemento', sa.String(length=45), nullable=False),
    sa.Column('modelo_elemento', sa.String(length=45), nullable=True),
    sa.ForeignKeyConstraint(['legajo_personal'], ['personal.legajo_personal'], ),
    sa.PrimaryKeyConstraint('id_numeracion_elementos')
    )
    op.create_table('herramientas_a_cargo',
    sa.Column('id_herramientas_a_cargo', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('legajo_personal', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['legajo_personal'], ['personal.legajo_personal'], ),
    sa.PrimaryKeyConstraint('id_herramientas_a_cargo')
    )
    op.create_table('herramientas_a_prestamo',
    sa.Column('id_herramientas_a_prestamo', sa.Integer(), nullable=False),
    sa.Column('legajo_personal', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=True),
    sa.Column('herramienta', sa.String(length=45), nullable=True),
    sa.Column('observaciones', sa.String(length=45), nullable=True),
    sa.Column('fecha_devolucion', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['legajo_personal'], ['personal.legajo_personal'], ),
    sa.PrimaryKeyConstraint('id_herramientas_a_prestamo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('herramientas_a_prestamo')
    op.drop_table('herramientas_a_cargo')
    op.drop_table('elementos_numerados')
    op.drop_table('control_diario')
    op.drop_table('stock')
    op.drop_table('personal')
    op.drop_table('talles_epp')
    op.drop_table('sector')
    op.drop_table('elementos')
    op.drop_table('tipo_vestimenta_epp')
    op.drop_table('matafuegos_recarga')
    op.drop_table('matafuegos')
    op.drop_table('categorias_inventario')
    op.drop_table('area')
    # ### end Alembic commands ###
