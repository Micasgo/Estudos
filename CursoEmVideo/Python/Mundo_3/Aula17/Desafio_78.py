"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []

for i in range (5):

    while True:
        try:
            lista.append(int(input("Digite um número")))
        except ValueError:
            print("\nValor não reconhecido, tente novamente\n")
        else: break
maior = max(lista)
menor = min(lista)
print(f"Sua lista foi {lista}\n")

print(f"O maior elemento foi {maior}, encontrado no índice ",end="")
for pos, n in enumerate(lista):
    if n == maior:
        print(pos,"",end="")
print()
print(f"O menor elemento foi {menor}, encontrado no índice ", end="")
for pos, n in enumerate(lista):
    if n == menor:
        print(pos,"",end="")
print()