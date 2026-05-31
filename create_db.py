from src.database.base import Base
from src.database.connection import engine

from src.models.categoria import Categoria
from src.models.cliente import Cliente
from src.models.endereco import Endereco
from src.models.entrega import Entrega
from src.models.item_pedido import ItemPedido
from src.models.motorista import Motorista
from src.models.pedido import Pedido
from src.models.produto import Produto
from src.models.veiculo import Veiculo


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Banco de dados criado com sucesso.")

# Por que importamos todos os modelos?
# O SQLAlchemy só cria as tabelas que foram registradas na Base.

# Com esse comando: poetry run python create_db.py irá criar o banco de dados.
# Execute-o pelo terminal