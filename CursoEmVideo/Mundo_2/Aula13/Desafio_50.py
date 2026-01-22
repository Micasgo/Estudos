"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar desconsidere-o.
"""


lista = []
cont = 0
soma = 0

"""
numeros = int(input("Quantos números serão lidos?: "))
for i in range(numeros):
    n = int(input("Digite um número: "))
    lista.append(n)

for n in lista:
    if n % 2 == 0:
        soma += n

print(f"A soma dos números pares escolhidos foi de {soma}")
"""

numeros = int(input("Quantos números serão lidos?: "))

for i in range (numeros):
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f"De {numeros} número(s) {cont} são pares e sua soma é igual a {soma}")