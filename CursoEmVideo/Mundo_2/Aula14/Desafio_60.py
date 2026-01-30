"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
"""

num = int(input("Coloque o número para fazer o fatorial: "))
cont = num
fat = num
lista = []

while cont != 1 and cont != 0:
    lista.append(str(cont))
    fat *= cont-1
    cont -= 1
    
if cont == 0:
    fat = 1

print(f"{num}! = {'x'.join(lista)}x1 que é igual a {fat}")

"""
num = int(input("Coloque o número para fazer o fatorial: "))
fat = num 
for i in range(1, num):
    fat *= i

print(f"{num}! é igual a {fat}")
"""