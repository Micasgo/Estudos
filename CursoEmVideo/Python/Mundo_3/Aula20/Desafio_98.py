"""
Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada
"""
from time import sleep
def intinput(pergunta=str):
    while True:
        try:valor = int(input(f"{pergunta}: "))
        except ValueError: print("\nValor não reconhecido")
        else: break
    return valor

def contagem():
    print("-="*12)
    for i in range (1,11):
        print(f"{i}", end=" ", flush=True)
        sleep(0.2)
    print()
    print("-="*12)

    for i in range (10,-1,-2):
        print(f"{i}", end=" ", flush=True)
        sleep(0.2)
    print()    
    print("-="*12)
    print("Vamos criar uma contagem personalizada!\n")
    inicio = intinput("Início")
    fim = intinput("Fim")
    passo = intinput("Passo")
    if passo == 0:
        if fim < inicio: passo = -1
        if fim > inicio: passo = 1
    print()
    for i in range (inicio, fim+1, passo):
        print(f"{i}", end=" ", flush=True)
        sleep(0.2)
    print()
    print("-="*12)

contagem()