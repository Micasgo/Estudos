"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.
"""

from random import randint
jogos = {}
cont = 0
jogadores = int(input("Quantos jogadores no jogo?"))


for i in range(jogadores):
    jogos[f"Jogador_{i+1}"] = randint(1,6)

jogos_seq1 = dict(sorted(jogos.items(), key = lambda items: (-items[1], items[0])))

verifica = None
for c,v in jogos_seq1.items():
        cont += 1
        print(f"O {cont}° lugar é o {c}, com {v} no dado!")
