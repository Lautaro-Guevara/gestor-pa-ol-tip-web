from app import db
from .area import Area
from .categorias_inventario import CategoriasInventario
from .control_diario import ControlDiario
from .elementos_numerados import ElementosNumerados
from .elementos import Elementos
from .herramientas_cargo import HerramientasACargo
from .herramientas_prestamo import HerramientasAPrestamo
from .matafuegos_recarga import MatafuegosRecarga
from .matafuegos import Matafuegos
from .personal import Personal
from .sector import Sector
from .stock import Stock
from .talles_epp import TallesEpp
from .tipo_vestimenta import TipoVestimentaEpp


"""
Para generar una migracion (Modificacion de la base de datos) se debe escribir el siguiente comado en la terminal:
    flask db migrate -m "Descripcion del cambio"

Para sincronizar los cambios en la base de datos se debe escribir el siguiente comando en la terminal:
    flask db upgrade

"""