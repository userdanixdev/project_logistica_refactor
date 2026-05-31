from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Produto(Base):
    __tablename__ = "produto"

    id_produto: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)

    preco_unitario: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    id_categoria: Mapped[int] = mapped_column(
        ForeignKey("categoria.id_categoria", ondelete="RESTRICT"),
        nullable=False,
    )

    categoria = relationship(
        "Categoria",
        back_populates="produtos",
    )

    itens = relationship(
        "ItemPedido",
        back_populates="produto",
    )

# O que esse modelo representa:
# A tabela produto guarda os produtos vendidos ou transportados.
# Campos:
# id_produto: chave primária
# nome: nome do produto
# preco_unitario: preço unitário do produto
# id_categoria: categoria à qual o produto pertence

# A regra do "ForeignKey("categoria.id_categoria", ondelete="RESTRICT")" significa:
# uma categoria não deve ser apagada se ainda existir produto vinculado a ela.