"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""
from time import sleep

for i in range(10,0,-1):
    print(f"\033[;32m{i}!\033[m")
    sleep(1)

print("Feliz Ano Novo!")

