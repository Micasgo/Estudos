"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint

while True:
    try: jogos = int(input("Quantos jogos serão jogados?: "))
    except ValueError: print("Valor não reconhecido")
    else: break

lista = list([]for i in range(jogos))

for j in range(jogos):
    for s in range(6):
        while True:
            n = randint(1,60)
            if n not in lista[j]:
                lista[j].append(n)
                break
    lista[j].sort()
    print(f"{j+1}° Jogo: {lista[j]}")
