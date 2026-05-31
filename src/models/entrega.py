from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Entrega(Base):
    __tablename__ = "entrega"

    id_entrega: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    id_pedido: Mapped[int] = mapped_column(
        ForeignKey("pedido.id_pedido", ondelete="CASCADE"),
        nullable=False,
    )

    id_motorista: Mapped[int] = mapped_column(
        ForeignKey("motorista.id_motorista", ondelete="RESTRICT"),
        nullable=False,
    )

    id_veiculo: Mapped[int] = mapped_column(
        ForeignKey("veiculo.id_veiculo", ondelete="RESTRICT"),
        nullable=False,
    )

    data_entrega: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    pedido = relationship(
        "Pedido",
        back_populates="entregas",
    )

    motorista = relationship(
        "Motorista",
        back_populates="entregas",
    )

    veiculo = relationship(
        "Veiculo",
        back_populates="entregas",
    )

# O que esse modelo representa:
# A tabela entrega registra a execução logística do pedido.
# Ela conecta:

# um pedido
# um motorista
# um veículo
# uma data de entrega

# Regras "ForeignKey("pedido.id_pedido", ondelete="CASCADE")" 
# Se o pedido for apagado, a entrega também pode ser apagada."

# A regra "ForeignKey("motorista.id_motorista", ondelete="RESTRICT")"
# "ForeignKey("veiculo.id_veiculo", ondelete="RESTRICT")"
# Motorista e veículo não devem ser apagados se já participaram de entregas, 
# porque isso preserva o histórico operacional.

