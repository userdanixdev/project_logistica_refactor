from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Veiculo(Base):
    __tablename__ = "veiculo"

    id_veiculo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    placa: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    tipo: Mapped[str] = mapped_column(String(40), nullable=False)

    entregas = relationship(
        "Entrega",
        back_populates="veiculo",
    )

# O que esse modelo representa:
# A tabela veiculo guarda os veículos usados nas entregas.
# Campos:
# id_veiculo: chave primária
# placa: identificação única do veículo
# tipo: tipo do veículo, como Van, Caminhão, Moto
# A placa foi definida como String, não como número, porque é um identificador.

# A regra do relationship é: Um veículo pode estar vinculado a várias entregas