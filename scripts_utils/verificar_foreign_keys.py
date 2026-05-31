from sqlalchemy import inspect
from src.database.connection import engine

def main() -> None:
    inspector = inspect(engine)
    for tabela in sorted(inspector.get_table_names()):
        foreign_keys = inspector.get_foreign_keys(tabela)

        print(f"\nTabela: {tabela}")

        if not foreign_keys:
            print(" Sem chaves estrangeiras.")
            continue

        for fk in foreign_keys:
            colunas_locais = ", ".join(fk["constrained_columns"])
            tabela_referenciada = fk["referred_table"]
            colunas_referenciadas = ", ".join(fk["referred_columns"])

            print(
                f" - {colunas_locais} -> "
                f" {tabela_referenciada}({colunas_referenciadas})"
            )

if __name__ == "__main__":
    main()