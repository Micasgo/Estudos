"""
Crie um programa que vai ler vários e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = []

while True:
    while True:
        try:
            num = int(input("Que número deseja colocar?: "))
            lista.append(num)
        except ValueError:
            print("\nValor não reconhecido\n")
        else: break
    while True:
        while True:
            try:
                condição = input("Quer continuar? (S/N)?: ").strip().upper()[0]
            except IndexError:
                print("Valor não reconhecido")
            else:break
        if condição not in "SN":
            print("\nOpção Inválida\n")
        else: break

    if condição == "N": break

lista.sort(reverse=True)

print(f"Sua lista é {lista}")

if 5 in lista:
    print(f"O número 5 está na lista, no índice {lista.index(5)}")
else: print ("O número 5 não está na lista")
