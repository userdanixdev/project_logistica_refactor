from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base


class Categoria(Base):
    __tablename__ = "categoria"

    id_categoria: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(String(80), nullable=False, unique=True)

    produtos = relationship(
        "Produto",
        back_populates="categoria",
    )

# O que esse modelo representa:
# A tabela categoria classifica os produtos.
# Campos:
# id_categoria: chave primária // descricao: nome da categoria, como Eletrônicos, Móveis, Alimentos
# Pontos principais:
#  'unique=True' impede que categoria duplicada tenha a mesma descrição.
# A entidade categoria jamais terá o mesmo id por ser autoincrement e chave primária
# O relacionamento categoria pode estar associada a vários produtos

