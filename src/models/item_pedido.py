from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class ItemPedido(Base):
    __tablename__ = "item_pedido"

    __table_args__ = (
        UniqueConstraint(
            "id_pedido",
            "id_produto",
            name="uq_item_pedido_produto",
        ),
    )

    id_item_pedido: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_pedido: Mapped[int] = mapped_column(
        ForeignKey("pedido.id_pedido", ondelete="CASCADE"),
        nullable=False,
    )

    id_produto: Mapped[int] = mapped_column(
        ForeignKey("produto.id_produto", ondelete="RESTRICT"),
        nullable=False,
    )

    quantidade: Mapped[int] = mapped_column(nullable=False)

    pedido = relationship(
        "Pedido",
        back_populates="itens",
    )

    produto = relationship(
        "Produto",
        back_populates="itens",
    )

# O que esse modelo representa:
# A tabela item_pedido representa os produtos dentro de um pedido.
# Ela resolve a relação entre pedido e produto.

# id_item_pedido: chave primária
# id_pedido: pedido ao qual o item pertence
# id_produto: produto vendido
# quantidade: quantidade do produto no pedido

# A regra "ForeignKey("pedido.id_pedido", ondelete="CASCADE")" significa:
# se o pedido for apagado, seus itens também são apagados.

# A regra "ForeignKey("produto.id_produto", ondelete="RESTRICT")" significa:
# um produto não deve ser apagado se já aparece em algum pedido.

# A restrição "UniqueConstraint("id_pedido", "id_produto")" 
# evita repetir o mesmo produto duas vezes dentro do mesmo pedido.