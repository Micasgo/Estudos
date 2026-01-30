"""
Escreva um programa que leia um número n inteiro qualquer e
mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
"""

sequencia = ["0","1"]
num = 1
cont = 1

lim = int(input("Quantos elementos da sequência de Fibonacci quer ver?: "))

while cont < lim:
    sequencia.append(str(num))
    num += int(sequencia[len(sequencia)-2])
    cont += 1

sequencia.remove(sequencia[len(sequencia)-1])

print(f"\nOs {lim} primeiros elementos da Sequência é: {", ".join(sequencia)}\n")
