#  📝 Anotações sobre Poetry

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![Poetry](https://img.shields.io/badge/Poetry-Ambiente%20e%20Dependencias-60A5FA)
![Status](https://img.shields.io/badge/Status-Anotacoes%20do%20Projeto-yellow)

## 📦 O que é o Poetry?

O Poetry é uma ferramenta para gerenciar projetos Python.

Ele ajuda em três pontos principais:

1. Criar e organizar o ambiente virtual do projeto.
2. Instalar e registrar as dependências utilizadas.
3. Manter o projeto reproduzível para outras pessoas ou outros computadores.

## 🧭 Por que usar Poetry neste projeto?

Neste projeto de logística, usamos Python com bibliotecas como SQLAlchemy, Pandas, OpenPyXL, Streamlit e Pytest.

Sem uma ferramenta de gerenciamento, cada pessoa poderia instalar versões diferentes dessas bibliotecas, causando erros difíceis de reproduzir.

Com o Poetry, as dependências ficam declaradas no arquivo `pyproject.toml`.

Assim, outra pessoa pode clonar o projeto e executar:

```powershell
poetry install
```

## 🐍 O que é um ambiente virtual?

Um ambiente virtual é um espaço isolado para instalar as bibliotecas de um projeto.

> Isso evita misturar as dependências deste projeto com as dependências de outros projetos Python instalados no computador.

### 💡 Exemplo:

```
Projeto de logística usa SQLAlchemy e Streamlit.
Outro projeto pode usar outras versões dessas bibliotecas.
O ambiente virtual evita conflito entre eles.
```

### 📄  Arquivos importantes do Poetry:

```pyproject.toml```

- É o arquivo principal de configuração do projeto.

### Nele ficam informações como:

- nome do projeto
- versão
- descrição
- versão do Python
- dependências principais
- dependências de desenvolvimento

```poetry.lock```

```
É o arquivo que registra exatamente quais versões foram instaladas.
Ele ajuda a garantir que o projeto rode da mesma forma em outro ambiente.
```

## 🧰 Comandos principais:

Verificar se o Poetry está instalado:

```poetry --version```

### ⚙️ Configurar o Poetry para criar o ambiente virtual dentro da pasta do projeto:

```poetry config virtualenvs.in-project true```

### 📥Instalar as dependências do projeto:

```
poetry install
```

### ➕ Adicionar uma nova dependência:

```poetry add nome-da-biblioteca```

### 🧪 Adicionar uma dependência apenas para desenvolvimento:

```poetry add --group dev nome-da-biblioteca```

### ▶️ Executar um comando dentro do ambiente virtual:

```poetry run python create_db.py```

### 🌐 Rodar a aplicação Streamlit:

```poetry run streamlit run src/app.py```

### ✅ Resumo:

> O Poetry serve para deixar o projeto Python mais organizado, isolado e reproduzível.

*Neste projeto, ele será usado para controlar o ambiente e garantir que as dependências necessárias estejam documentadas e instaladas corretamente.*

---

## 🛠️ Passo a passo realizado:

### 1. Iniciei o projeto com Poetry:

```powershell
poetry init
```

Esse comando criou o arquivo ```pyproject.toml```, que centraliza as configurações do projeto Python.

### 2. Configurei o Poetry para criar o ambiente virtual dentro da pasta do projeto:

```poetry config virtualenvs.in-project true```

> *Com isso, o ambiente virtual fica em .venv/, facilitando a visualização no VS Code.*

### 3. Instalei o SQLAlchemy:

```poetry add sqlalchemy```

> *O SQLAlchemy será usado para mapear as tabelas do banco relacional usando ORM.*

### 4. Instalei Pandas e OpenPyXL:

```poetry add pandas openpyxl```

> *O Pandas será usado para manipular dados e o OpenPyXL permite ler arquivos Excel .xlsx.*

### 5. Instalei o Streamlit:

```poetry add streamlit```

> *O Streamlit será usado para criar o painel web da aplicação.*

### 6. Instalei o Pytest como dependência de desenvolvimento:

```poetry add --group dev pytest```

> *O Pytest será usado futuramente para criar testes e validações do projeto.*

---

## 🔎 Validações iniciais do banco:

Depois de criar os modelos ORM e executar:

```powershell
poetry run python create_db.py
```
foram criados scripts utilitários para validar o banco.

### 📋 ```verificar_banco.py```

Lista as tabelas existentes no banco:

```poetry run python scripts_utils\verificar_banco.py```

### Objetivo:

- confirmar que o banco foi criado
- confirmar que as tabelas esperadas existem

### 🧱 - verificar_schema.py

Mostra as colunas, tipos, nulidade e chaves primárias de cada tabela:

```
poetry run python scripts_utils\verificar_schema.py
```

### Objetivo:

- conferir se o modelo físico foi criado corretamente
- validar tipos de dados
- validar campos obrigatórios

### 🔗- verificar_foreign_keys.py

### Lista as chaves estrangeiras de cada tabela:

```
poetry run python scripts_utils\verificar_foreign_keys.py
```

### Objetivo:

- conferir os relacionamentos entre as tabelas
- validar os vínculos do modelo relacional

### 🛡️ - verificar_sqlite_fk.py

###  Confirma se o SQLite está com chaves estrangeiras ativadas:

```
poetry run python scripts_utils\verificar_sqlite_fk.py
```

### Resultado esperado:

```
PRAGMA foreign_keys = 1
Chaves estrangeiras estão ATIVADAS no SQLite.
```

> *Assim garantir que regras como CASCADE e RESTRICT sejam aplicadas no SQLite*

# 🚚 Project Logistica Refactor:

## Descrição:

Este projeto tem como objetivo desenvolver uma aplicação para consultar dados logísticos normalizados.

O estudo parte de um cenário fictício no qual uma empresa possui uma planilha de entregas oriunda de um ambiente transacional. A proposta é transformar esses dados em um modelo relacional normalizado, com entidades como:

- clientes
- endereços
- produtos
- categorias
- pedidos
- itens de pedido
- entregas
- motoristas
- veículos

A modelagem busca garantir:

- integridade referencial
- normalização dos dados
- preservação de informações históricas
- base para consultas analíticas

