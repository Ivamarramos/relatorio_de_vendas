# Gerador de Relatório de Vendas em Excel

É um Script em Python que lê um arquivo CSV de vendas e gera uma planilha Excel formatada, com resumo geral e análises por produto, mês e vendedor.

## Como usar

1. Instale o Python 3 e crie o ambiente virtual:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Gere dados de exemplo (opcional) e o relatório:

```
python gerar_dados.py
python relatorio.py
```

3. Abra o arquivo `relatorio_vendas.xlsx`.

## Para usar com seus dados

Substitua o `vendas.csv` por um arquivo com as colunas:
`data, produto, quantidade, preco_unitario, vendedor`.

## Tecnologias

- Python 3
- pandas
- openpyxl

## Observação

Os dados deste projeto são fictícios apenas para exemplificações.

## Autor

Ivamar Ramos - [GitHub](https://github.com/Ivamarramos)