"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
cont = 0

print("\033[;32mVamos jogar um jogo!\033[m\n")
print("--"*10)
while True:
    jogador = input("\n\033[;32mPar\033[m ou \033[;33mímpar\033[m?(P/I): ").strip().upper().replace("Í", "I")[0]
    print("--"*10)
    if jogador == "P": print("\nVou de \033[;33mímpar\033[m então!")
    elif jogador == "I": print("\nVou de \033[;32mpar\033[m então!")
    else:
        while jogador not in "PI":
            print("--"*10)
            print("\nOu é par ou é impar, não tem outra")
            jogador = input("\n\033[;32mPar\033[m ou \033[;33mímpar\033[m?(P/I): ").strip().upper().replace("Í", "I")[0]
            print("--"*10)
    num = int(input("\nJogue seu número: "))
    bot = randint(0,10)
    soma = bot + num
    print(f"\nO bot escolheu {bot}")
    print("--"*10)
    if jogador == "P" and soma % 2 == 0:
        print(f"\nVocê \033[;32mGanhou!\033[m {soma} é par!")
        cont += 1
    elif jogador == "I" and soma % 2 != 0:
        print(f"\nVocê \033[;32mGanhou!\033[m {soma} é impar!")
        cont += 1
    else:
        print("\nHAHAHA, você \033[;31mPERDEU\033[m")
        break
    print("-="*10)

if cont > 0:
    print(f"\n\033[;32mParabêns!\033[m Você conseguiu \033[;32m{cont} vítoria(s)!\033[m")
else:
    print("\nPerdeu na primeira? ... \033[;31mFRACO\033[m")