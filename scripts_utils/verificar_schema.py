from sqlalchemy import inspect
from src.database.connection import engine

def main() -> None:
    inspector = inspect(engine)
    for tabela in sorted(inspector.get_table_names()):
        print(f"\nTabela: {tabela}")

        colunas = inspector.get_columns(tabela)
        for coluna in colunas:
            nome = coluna["name"]
            tipo = coluna["type"]
            nullable = coluna["nullable"]
            chave_primaria = coluna["primary_key"]

            print(
                f" - {nome} | {tipo}  | "
                f"nullable={nullable} | pk={chave_primaria}"
            )
if __name__ == "__main__":
    main()