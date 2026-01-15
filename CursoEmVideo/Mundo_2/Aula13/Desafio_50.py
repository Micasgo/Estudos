"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.
"""

numeros = int(input("Quantos números serão lidos?: "))
lista = []
soma = 0

for i in range(numeros):
    n = int(input("Digite um número: "))
    lista.append(n)

for index in range(len(lista)):
    if lista[index] % 2 == 0:
        soma += lista[index]

print(f"A soma dos números pares escolhidos foi de {soma}")
