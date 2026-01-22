"""
Melhore o jogo do Desafio 28 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""
from time import sleep
from random import randint

chute = -1
num = 0
tentativas = 0

print("\033[;32m\nVamos jogar um jogo!\n\033[m","-="*10)
sleep(1)
print("\nVou pensar em um número entre 1 e 10")
sleep(1)

while chute != num:
    num = randint(1,10)
    chute = int(input("\nAdivinhe o número que eu estou pensando agora: "))
    if num == chute:
        print("\n\033[;32mParabêns você acertou!\033[m")
        tentativas += 1
    else:
        print(f"\nErrado, eu pensei no número {num}")
        tentativas += 1

print(f"\nForam {tentativas} tentativas")