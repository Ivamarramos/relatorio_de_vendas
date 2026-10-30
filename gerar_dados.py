import csv
import random
from datetime import date, timedelta

random.seed(42)

PRODUTOS = {
    "Caneta": 2.50,
    "Caderno": 18.90,
    "Mochila": 89.90,
    "Mouse": 45.00,
    "Teclado": 120.00,
    "Fone de ouvido": 75.50,
}

VENDEDORES = ["Ana", "Bruno", "Carla", "Diego"]
DATA_INICIAL = date(2026, 1, 1)
TOTAL_VENDAS = 200

with open("vendas.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["data", "produto", "quantidade", "preco_unitario", "vendedor"])
   
    for _ in range(TOTAL_VENDAS):
       dia = DATA_INICIAL + timedelta(days=random.randint(0, 270))
       produto = random.choice(list(PRODUTOS))
       quantidade = random.randint(1, 5)
       preco = PRODUTOS[produto]
       vendedor = random.choice(VENDEDORES)
       escritor.writerow([dia.isoformat(), produto, quantidade, preco, vendedor])
       
print(f"vendas.csv criado com {TOTAL_VENDAS} vendas.")

 