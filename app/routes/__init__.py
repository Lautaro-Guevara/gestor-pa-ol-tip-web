# app/routes/__init__.py
from .main import index_bp
from .lista_personal import lista_personal_bp
from .entregas_diarias import entregas_diarias_bp
from .matafuegos import matafuegos_bp
from .stock_bp import stock_bp


__all__ = ["index_bp", "lista_personal_bp","entregas_diarias_bp","matafuegos_bp","stock_bp"]