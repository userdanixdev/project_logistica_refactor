from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

# O que esse arquivo faz:

# A classe Base é a base de todos os modelos ORM.
# Cada tabela do banco será representada por uma classe Python que herda de Base.