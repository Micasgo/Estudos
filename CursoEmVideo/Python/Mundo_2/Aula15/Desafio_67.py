"""
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
"""


num = int(input("Digite um número para a tabuada. (Digite um número menor que 0 para parar): "))

while True:
    if num < 0: break
    print("-="*15)
    for i in range(10):
        print(f"{num} * {i+1} = \033[;32m{(i+1)*num}\033[m")
    print("-="*15)
    num = int(input("Digite um número para fazer a tabuada: "))
