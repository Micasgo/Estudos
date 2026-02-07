"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
valores únicos digitados, em ordem crescente.
"""
lista = []

while True:
    while True:
        try:
            num = int(input("Qual número deseja colocar?: "))
        except ValueError:
            print("\nValor não reconhecido, tente novamente\n")
        else: break
    if num in lista:
        None
    else: lista.append(num)
    while True:
        condicao = input("Quer continuar? (S/N): ").strip().upper()[0]
        if condicao not in "SN":
            print("\nOpção inválida\n")
        else: break
    if condicao == "N": break

lista.sort()
print(lista)