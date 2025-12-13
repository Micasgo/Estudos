# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
num = randint(0,5)

escolha = int(input("Escolha um número entre 0 e 5 e tente acertar o número que foi escolhido: "))

if escolha == num:
    print("Você acertou, parabêns!")
else:
    print("Você é burro(a), havia escolhido o número", num)
