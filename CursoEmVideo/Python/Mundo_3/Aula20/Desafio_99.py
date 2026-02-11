"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*num):
    for pos, n in enumerate(num):
        if pos == 0:
            maior = n
        if n > maior: maior = n
    print(f"O maior destes números {num} é: {maior}") 

maior(-1,0)