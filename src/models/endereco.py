from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.base import Base

class Endereco(Base):
    __tablename__ = "endereco"
    __table_args__=(
        UniqueConstraint(
        "id_cliente",
            "logradouro",
            "numero",
            "cidade",
            "estado",
            name="uq_endereco_cliente_local",
        ),)
    id_endereco: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    id_cliente: Mapped[int] = mapped_column(
        ForeignKey("cliente.id_cliente",ondelete="CASCADE"),nullable=False)
    logradouro: Mapped[str] = mapped_column(String(120), nullable=False)
    numero: Mapped[str] = mapped_column(String(10), nullable=False)
    cidade: Mapped[str] = mapped_column(String(80), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)

    cliente = relationship("Cliente",back_populates="enderecos")

# O que esse modelo representa:
# A tabela endereco guarda os endereços vinculados a clientes.
# Campos principais:
# id_endereco: chave primária // id_cliente: chave estrangeira para cliente 
# logradouro, numero, cidade, estado: dados do endereço
    
# 'ondelete="CASCADE" -> se um cliente for apagado, os endereços dele também podem ser apagados.
# UniqueConstraint(...) evita cadastrar o mesmo endereço para o mesmo cliente