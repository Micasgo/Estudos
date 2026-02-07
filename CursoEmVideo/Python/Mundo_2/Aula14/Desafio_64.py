"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números forma digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

soma = 0
num = 0
lista = []
cont = 0

while num != 999:
    soma += num
    num = int(input("Que número você quer somar?: "))
    lista.append(str(num))
    cont += 1
lista.remove(lista[len(lista)-1])

print(f"A soma dos {cont} números: {", ".join(lista)}\n\nFoi {soma}")