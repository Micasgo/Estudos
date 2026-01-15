"""
Faça um programa que calcule a soma entre todos os números ímpares
que são múltiplos de três e que se encontram no intervalo de 1 até 500
"""

alcance = int(input("Qual o alcance da medição?: "))

print(f"A soma de todos os números ímpares múltiplos de três de 0 a {alcance} é:")

soma = 0

for i in range(alcance+1):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print(soma)