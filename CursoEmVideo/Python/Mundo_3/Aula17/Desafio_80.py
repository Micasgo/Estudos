"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort())
No final, mostre a lista ordenada na tela.
"""

lista = []

for i in range(5):
    while True:
        try:
            num = int(input("Digite um número"))
        except ValueError:
            print("\nValor não reconhecido\n")
        else:break
    if i == 0:
        lista.append(num)
        print("Valor adicionado no índice 0\n")
    else:
        for n in range(len(lista)):
            if num <= lista[n]:
                print(f"Valor adicionado no índice {n}\n")
                lista.insert(n,num)
                break
        if num > lista[-1]:
            print(f"Valor adicionado ao final da lista\n")
            lista.append(num)

print(lista)
