"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e menor peso lidos
"""

pessoas = int(input("Quantas pessoas serão analisadas?").strip())
lista = []
"""
for i in range(pessoas):
    peso = float(input(f"Qual o peso da {i+1}° pessoa? (em Kg): ").strip().replace(",","."))
    lista.append(peso)

print(f"O maior peso foi da {lista.index(max(lista))+1}° pessoa, com {max(lista)} Kg")
print(f"O menor peso foi de {lista.index(min(lista))+1}° pessoa, com {min(lista)} Kg")
"""

maior = 0
menor = 0

for i in range(pessoas):
    peso = float(input(f"Qual o peso da {i+1}° pessoa? (em Kg): ").strip().replace(",","."))
    if i == 0:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"O mais pesado tem {maior}kg, o menor {menor} kg")