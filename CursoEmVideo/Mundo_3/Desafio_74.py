"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerado e também indique o menor e maior valor que estão na tupla
"""
from random import randint

tupla = tuple(randint(0,9) for i in range(5))

print(tupla)

"""
print(f"O maior número é {max(tupla)}")
print(f"O menor número é {min(tupla)}")
"""

for pos,n in enumerate(tupla):
    if pos == 0:
        maior = n
        menor = n
    if n > maior: maior = n
    if n < menor: menor = n

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")