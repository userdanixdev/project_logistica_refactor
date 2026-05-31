import logging
from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///database_logistic.db"

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "sqlalchemy.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logging.getLogger("sqlalchemy.engine").setLevel(logging.DEBUG)

def build_engine(database_url: str = DATABASE_URL, echo: bool = False):
    engine = create_engine(
        database_url,
        echo=echo,
        future = True,
    )
    if database_url.startswith("sqlite"):
        @event.listens_for(engine,"connect")
        def activate_keys_foreign_sqlite(dbapi_connection, connection_record):
            cursor=dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()
    return engine            

# criamos build_engine() para o pytest executar. Dessa forma os testes conseguem criar um banco temporário separado
# o projeto continua usando database_logistic.db normalmente.

engine = create_engine(
    DATABASE_URL,
    echo = False,
    future=True,
)
# Decorador em que SQLAlchemy ao abrir uma conexão com o banco executa o event
# No SQLite, as regras de chave estrangeira existem, mas não ficam ativas automaticamente em todas as conexões.
# Dessa forma as regras de 'RESTRICT' E 'CASCADE' NÃO FUNCIONAM
@event.listens_for(engine,"connect")
def habilitar_sqlite_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)

# O que esse arquivo faz:

# cria a conexão com o banco SQLite
# define que o banco será database_logistic.db
# ativa as chaves estrangeiras no SQLite
# cria SessionLocal, que será usado para inserir, consultar e manipular dados