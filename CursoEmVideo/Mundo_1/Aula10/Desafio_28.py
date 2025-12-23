# Escreva um programa que faça o computador "pensar" em um número
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep


num = randint(0,5)


print("-~~-"*10,"\n Que número eu pensei? Tente adivinhar.\n","-~~-"*10,"\n")

escolha = int(input("Escolha um número entre 0 e 5 e tente acertar o número que foi escolhido: "))

print("Processando...")
sleep(2)

if escolha == num:
    print("Você acertou, parabêns!")
else:
    print("Você é burro(a), havia escolhido o número", num)
