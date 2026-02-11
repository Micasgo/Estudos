"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia()
e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista
e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
"""

numeros = []

def sorteia(lista, numeros=5):
    from random import randint
    for i in range(numeros):
        lista.append(randint(0,9))
    print(lista)
def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(soma)

sorteia(numeros,10)
somapar(numeros)
