"""
Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você
"""

from random import randint
from time import sleep

print("-~"*18, "\n\033[;32mVamos jogar pedra papel e tesoura!\033[m\n","-~"*18)
sleep(1)
print("Melhor de 3!")

pontosR = 0
pontosV = 0

for jogadas in range (3):
    robo = randint(1,3)

    for i in range (3):
        print(f"{3-i}")
        sleep(1)

    mao = input("Escolha sua jogada!\n\n:").lower().strip()

    if robo == 1 and mao == "pedra":
        print("\nEu escolho pedra!\n\nAh, empatamos\n")
    elif robo == 1 and mao == "papel":
        print("\nEu escolho pedra!\n\nAh você ganhou :(\n")
        pontosV += 1
    elif robo == 1 and mao == "tesoura":
        print("\nEu escolho pedra!\n\nÉ, ganhei!\n")
        pontosR += 1

    elif robo == 2 and mao == "papel":
        print("\nEu escolho papel!\n\nAh, empatamos\n")
    elif robo == 2 and mao == "tesoura":
        print("\nEu escolho papel!\n\nAh você ganhou :(\n")
        pontosV += 1
    elif robo == 2 and mao == "pedra":
        print("\nEu escolho papel!\n\nÉ, ganhei!\n")
        pontosR += 1
    
    elif robo == 3 and mao == "tesoura":
        print("\nEu escolho tesoura!\n\nAh, empatamos\n")
    elif robo == 3 and mao == "pedra":
        print("\nEu escolho tesoura!\n\nAh você ganhou :(\n")
        pontosV += 1
    elif robo == 3 and mao == "papel":
        print("\nEu escolho tesoura!\n\nÉ, ganhei!\n")
        pontosR += 1
    else:
        print("Você escreveu errado?")
    sleep(1)
    print(f"Você tem {pontosV} pontos e eu tenho {pontosR}")
    if jogadas != 2:
        print(f"Faltam {2-jogadas} rodadas!")
    sleep(1)
print("\n" + "="*30)
if pontosV > pontosR:
    print(f"\033[;32m{'Você venceu!'.center(30)}\033[m")
elif pontosR > pontosV:
    print("Eu venci, você não é páreo a minha sorte")
else:
    print("Empate '-'")
print("="*30,"\n")