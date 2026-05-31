# Project Logistica Refactor

## Descrição

Este projeto tem como objetivo desenvolver uma aplicação para consulta e análise de dados logísticos normalizados.

O estudo parte de um cenário fictício em que uma empresa possui uma planilha de entregas originada de um ambiente transacional. A proposta é transformar esses dados em um modelo relacional normalizado, organizando as informações em entidades como clientes, endereços, categorias, produtos, pedidos, itens de pedido, entregas, motoristas e veículos.

A modelagem foi elaborada para garantir integridade referencial, normalização dos dados e preservação de informações históricas.

## Objetivos

- Modelar um banco de dados relacional para um cenário logístico.
- Separar dados cadastrais e transacionais.
- Implementar modelos ORM com SQLAlchemy.
- Utilizar SQLite como banco local.
- Gerenciar dependências e ambiente com Poetry.
- Criar scripts utilitários para validação do banco.
- Evoluir o projeto para um painel web com Streamlit.

## Tecnologias

- Python
- Poetry
- SQLAlchemy
- SQLite
- Pandas
- OpenPyXL
- Streamlit
- Pytest
- Git e GitHub

## Estrutura do Projeto

```text
project_logistica_refactor/
├── data/
│   ├── raw/
│   ├── bronze/
│   └── silver/
├── scripts_utils/
├── src/
│   ├── database/
│   ├── etl/
│   └── models/
├── tests/
├── create_db.py
├── pyproject.toml
└── readme.md
```
## Modelagem de Dados

O projeto foi estruturado a partir de um processo de modelagem em camadas, partindo da compreensão conceitual do domínio até a implementação física do banco relacional.

### Modelo Conceitual

O modelo conceitual representa as principais entidades do cenário logístico e seus relacionamentos em alto nível.

![Modelo Conceitual](src/docs/model_concept_peter_chen_der.png)

### Modelo Lógico

O modelo lógico transforma as entidades do domínio em tabelas relacionais, definindo chaves primárias, chaves estrangeiras e relacionamentos entre as estruturas.

![Modelo Lógico](src/docs/model_logic_james_martin.png)

### Amostra da Tabela Central

A tabela central original representa a visão transacional antes do processo de normalização.

![Tabela Central](src/docs/tabela_central_sample.png)


Ambiente
Instale as dependências com Poetry:

poetry install
Ative o ambiente virtual no Git Bash:

source .venv/Scripts/activate
Ou execute comandos diretamente com Poetry:

poetry run python nome_do_script.py
Criação do Banco
Execute:

python create_db.py
Ou:

poetry run python create_db.py
O arquivo database_logistic.db será criado localmente.

Validações
Listar tabelas criadas:

python scripts_utils/verificar_banco.py
Verificar colunas, tipos, nulidade e chaves primárias:

python scripts_utils/verificar_schema.py
Verificar chaves estrangeiras:

python scripts_utils/verificar_foreign_keys.py
Verificar se as foreign keys estão ativas no SQLite:

python scripts_utils/verificar_sqlite_fk.py
Status da Versão
A versão inicial contempla:

configuração do projeto com Poetry
estrutura inicial de diretórios
conexão com SQLite
ativação de chaves estrangeiras no SQLite
modelos ORM com SQLAlchemy
script de criação do banco
scripts utilitários de validação
Próximos Passos
Implementar a camada Bronze.
Implementar a camada Silver.
Criar carga dos dados normalizados no banco.
Desenvolver o painel web com Streamlit.
Criar testes automatizados.
