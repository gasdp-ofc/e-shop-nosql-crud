from faker import Faker
from pymongo import MongoClient
from random import randint, choice
from datetime import datetime
import time

# Conexão com MongoDB (ajuste o host conforme necessário)
client = MongoClient("mongodb://localhost:27017/")
db = client["eshop"]
colecao = db["clientes"]

fake = Faker('pt_BR')

# Inserir em lotes para evitar sobrecarga
batch_size = 10000
total_registros = 1000000
dados = []

start_time = time.time()
for i in range(1, total_registros + 1):
    cliente = {
        "nome": fake.name(),
        "email": fake.email(),
        "telefone": fake.phone_number(),
        "endereco": fake.address(),
        "idade": randint(18, 75),
        "status": choice(["ativo", "inativo", "suspenso"]),
        "data_criacao": fake.date_time_this_decade().isoformat()
    }
    dados.append(cliente)

    if i % batch_size == 0:
        colecao.insert_many(dados)
        print(f"Inseridos {i} registros...")
        dados = []

# Inserir restantes
if dados:
    colecao.insert_many(dados)
    print(f"Inseridos os últimos {len(dados)} registros.")

print("✅ Inserção concluída em %.2f segundos." % (time.time() - start_time))
