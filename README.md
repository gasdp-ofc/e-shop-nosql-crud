# Integração de Soluções NoSQL com Streamlit para Visualização de Dados

Este projeto demonstra uma aplicação CRUD (Criar, Ler, Atualizar e Deletar) utilizando **MongoDB** como banco NoSQL e **Streamlit** como interface web, integrados em um ambiente containerizado via **Docker**. O objetivo é atender às necessidades da empresa fictícia **E-Shop Brasil**, que busca modernizar sua infraestrutura digital para manipulação de dados de forma escalável e visual.

---

## 🎯 Objetivo do Projeto

- Criar uma aplicação prática com interface interativa.
- Executar operações CRUD sobre um banco NoSQL (MongoDB).
- Inserir automaticamente **1 milhão de registros falsos** usando a biblioteca `Faker`.
- Garantir portabilidade usando `Docker Compose`.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.11**
- **Streamlit** – Interface gráfica
- **MongoDB** – Banco de dados NoSQL
- **Faker** – Geração de dados fictícios
- **Docker + Docker Compose** – Ambiente isolado e reprodutível

---

## 📁 Estrutura do Projeto

```
e-shop-nosql-crud/
├── app.py                        # Aplicação Streamlit com CRUD
├── docker-compose.yml           # Sobe MongoDB + dataloader + app
├── inserir_clientes_faker_mongo.py  # Gera 1 milhão de registros falsos
├── requirements.txt             # Dependências do Python
└── README.md                    # Este documento
```

---

## ⚙️ Como Executar o Projeto (Passo a Passo)

### 1. 🐋 Instale o Docker

Baixe e instale o Docker Desktop:  
🔗 https://www.docker.com/products/docker-desktop/

> Verifique se o Docker está rodando (ícone da baleia na barra de tarefas).

---

### 2. 📦 Extraia o Projeto

Descompacte o arquivo `e-shop-nosql-crud-completo.zip` e abra a pasta `e-shop-nosql-crud/` no seu terminal ou VS Code.

---

### 3. 🚀 Execute o Projeto com Docker Compose

No terminal, dentro da pasta do projeto, rode:

```bash
docker-compose up --build
```

Esse comando irá:
- Subir um container com o **MongoDB**
- Rodar o script `inserir_clientes_faker_mongo.py` dentro do container `dataloader`, gerando automaticamente **1 milhão de registros falsos**.
- Subir o app Streamlit na porta `8501`

---

### 4. 🌐 Acesse a Aplicação

Abra o navegador e acesse:

```
http://localhost:8501
```

Você verá a interface com as seguintes funcionalidades:

- **Criar:** formulário para adicionar novos clientes
- **Ler:** tabela com todos os clientes cadastrados
- **Atualizar:** campo para alterar nome a partir do email
- **Deletar:** excluir cliente pelo email

---

## 📊 Dados Simulados

O script `inserir_clientes_faker_mongo.py` utiliza a biblioteca **Faker** para gerar clientes com os seguintes campos:

- Nome
- Email
- Telefone
- Endereço
- Idade
- Status (ativo, inativo, suspenso)
- Data de criação

Esses dados são gerados em lotes de 10 mil registros para evitar sobrecarga e são inseridos automaticamente no banco MongoDB.

---

## 📌 Observações Importantes

- Certifique-se de que **nenhuma outra aplicação esteja usando a porta 27017 (MongoDB)** ou 8501 (Streamlit).
- Para reiniciar os containers sem cache:

```bash
docker-compose down
```

---

## 🤝 Contribuições

Este projeto pode ser adaptado para outros bancos NoSQL como **Clickhouse** ou front-ends como **Flask**, **React**, ou **FastAPI**.

Fique à vontade para customizar e melhorar para seu portfólio profissional!

---

## 📽️ Vídeo Demonstrativo

Sugestão para o vídeo de apresentação:

1. Mostrar a estrutura do projeto
2. Executar `docker-compose up` e exibir logs
3. Acessar o app no navegador
4. Inserir, atualizar e excluir um cliente
5. Mostrar a escala dos dados com scroll na tabela

---

**Desenvolvido por Guilherme | Projeto E-Shop Brasil**
