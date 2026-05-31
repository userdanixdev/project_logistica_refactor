from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Pedido(Base):
    __tablename__ = "pedido"

    id_pedido: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_cliente: Mapped[int] = mapped_column(
        ForeignKey("cliente.id_cliente", ondelete="RESTRICT"),
        nullable=False,
    )

    data_pedido: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    cliente = relationship(
        "Cliente",
        back_populates="pedidos",
    )

    itens = relationship(
        "ItemPedido",
        back_populates="pedido",
        cascade="all, delete-orphan",
    )

    entregas = relationship(
        "Entrega",
        back_populates="pedido",
        cascade="all, delete-orphan",
    )

# O que esse modelo representa:
# A tabela pedido registra os pedidos feitos pelos clientes.

# A regra "ForeignKey("cliente.id_cliente", ondelete="RESTRICT")" significa:
# um cliente não deve ser apagado se ele já possui pedidos. Preservando o histórico.

# Os relacionamentos:
# itens = relationship(...)
# entregas = relationship(...)

# um pedido pode ter vários itens e um pedido pode ter várias entregas.
# O cascade="all, delete-orphan" em itens e entregas significa:
# se um pedido for removido, seus itens e entregas também são removidos, porque não fazem sentido sem o pedido.