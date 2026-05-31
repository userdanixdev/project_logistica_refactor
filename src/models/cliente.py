from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    cpf: Mapped[str] = mapped_column(String(14), nullable=False, unique=True)

    enderecos = relationship(
        "Endereco",
        back_populates="cliente",
        cascade="all, delete-orphan",
    )
    pedidos = relationship(
        "Pedido",
        back_populates="cliente",
    )

# Observações importantes:
# O que esse modelo representa:
# A classe Cliente representa a tabela cliente.

# id_cliente: chave primária
# nome: nome do cliente
# cpf: identificador único do cliente
# Relacionamentos:

# um cliente pode ter vários endereços
# um cliente pode ter vários pedidos
# O cascade="all, delete-orphan" em enderecos significa:
# se um cliente for removido, seus endereços também serão removidos, porque endereço não faz sentido sem cliente.    