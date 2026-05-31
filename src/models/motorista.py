from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Motorista(Base):
    __tablename__ = "motorista"

    id_motorista: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    cnh: Mapped[str] = mapped_column(String(11), nullable=False, unique=True)

    entregas = relationship(
        "Entrega",
        back_populates="motorista",
    )

#  que esse modelo representa:
# A tabela motorista guarda os motoristas responsáveis pelas entregas.
# Campos: 
# id_motorista: chave primária
# nome: nome do motorista
# cnh: identificação do motorista
# A CNH foi definida como String, não como número, porque identificadores podem ter zeros à esquerda e 
# não devem ser usados em cálculos.

# A regra 'unique=True' impede cadastrar duas vezes a mesma CNH.

# O relacionamento 'entregas' significa que um motorista pode estar vinculado a várias entregas.