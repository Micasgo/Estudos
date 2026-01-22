"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores
"""
from datetime import datetime

maior = 0
pessoas = int(input("Quantas pessoas serão analisadas?: "))


for i in range(pessoas):
    nascimento = int(input(f"Ano de nascimento da {i+1}° pessoa: "))
    if datetime.today().year - nascimento >= 18:
        maior +=1

print(f"Dentre as {pessoas} pessoas, existem {maior} na maioridade e {pessoas - maior} na menoridade")