from sqlalchemy import inspect, text

from src.database.base import Base
from src.database.connection import build_engine

from src.models.categoria import Categoria
from src.models.cliente import Cliente
from src.models.endereco import Endereco
from src.models.entrega import Entrega
from src.models.item_pedido import ItemPedido
from src.models.motorista import Motorista
from src.models.pedido import Pedido
from src.models.produto import Produto
from src.models.veiculo import Veiculo

def test_tables_base_temp(tmp_path):
    db_path = tmp_path / "database_test.db"
    engine = build_engine(f"sqlite:///{db_path}", echo=False)
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)

    tabelas_esperadas = {
        "categoria",
        "cliente",
        "endereco",
        "entrega",
        "item_pedido",
        "motorista",
        "pedido",
        "produto",
        "veiculo",
    }
    assert set(inspector.get_table_names()) == tabelas_esperadas

def test_sqlite_foreign_key_base_temp(tmp_path):
    db_path = tmp_path / "database_test.db"
    engine = build_engine(f"sqlite:///{db_path}",echo=False)

    with engine.connect() as conn:
        resultado = conn.execute(text("PRAGMA foreign_keys")).scalar()

    assert resultado == 1

def test_keys_principais(tmp_path):
    db_path = tmp_path / "database_test.db"
    engine =  build_engine(f"sqlite:///{db_path}", echo=False)
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)

    fks_pedido = inspector.get_foreign_keys("pedido")
    fks_item = inspector.get_foreign_keys("item_pedido")
    fks_entrega = inspector.get_foreign_keys("entrega")

    assert any(fk["referred_table"] == "cliente" for fk in fks_pedido)

    assert any(fk["referred_table"] == "pedido" for fk in fks_item)
    assert any(fk["referred_table"] == "produto" for fk in fks_item)

    assert any(fk["referred_table"] == "pedido" for fk in fks_entrega)
    assert any(fk["referred_table"] == "motorista" for fk in fks_entrega)
    assert any(fk["referred_table"] == "veiculo" for fk in fks_entrega)
    