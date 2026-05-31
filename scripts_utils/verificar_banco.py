from sqlalchemy import inspect

from src.database.connection import engine


def main() -> None:
    inspetor = inspect(engine)
    tabelas = inspetor.get_table_names()

    print("Tabelas encontradas no banco:")
    for tabela in sorted(tabelas):
        print(f"- {tabela}")


if __name__ == "__main__":
    main()