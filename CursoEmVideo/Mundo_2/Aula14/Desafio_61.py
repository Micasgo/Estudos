"""
Refaça o Desafio 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

a1 = int(input("Qual o primeiro termo da P.A.?: "))
r = int(input("Qual a razão da P.A.?: "))
pa = int(input("Qual o tamanho da P.A.?: "))
termo1 = a1
lista = []

while termo1 != a1 + (r*(pa-1)):
    lista.append(str(termo1))
    termo1 += r
lista.append(str(a1 + (r*(pa-1))))


print(f"Sua P.A. é: {", ".join(lista)}")