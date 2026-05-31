from sqlalchemy import text

from src.database.connection import engine


def main() -> None:
    with engine.connect() as conn:
        resultado = conn.execute(text("PRAGMA foreign_keys")).scalar()

    print("PRAGMA foreign_keys =", resultado)

    if resultado == 1:
        print("Chaves estrangeiras estão ATIVADAS no SQLite.")
    else:
        print("Chaves estrangeiras estão DESATIVADAS no SQLite.")


if __name__ == "__main__":
    main()