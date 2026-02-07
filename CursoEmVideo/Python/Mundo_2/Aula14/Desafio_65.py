"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar mais valores.
"""

cont = 0
soma = 0
valormax = 0
valormin = 0
condicao = str
lista = []

while condicao != "N":
    cont += 1
    num = int(input("Qual o número que quer colocar?: "))
    soma += num
    if cont == 1:
        valormax = num
        valormin = num
    if valormax < num: valormax = num
    if valormin > num: valormin = num
    condicao = input("Quer continuar?(S/N): ").upper()[0]
    lista.append(str(num))
    
media = soma/cont

print(f"\nSeus números foram: {", ".join(lista)}")
print(f"\nA média de todos os valores é {media}, o maior valor é {valormax} e o menor é {valormin}")
