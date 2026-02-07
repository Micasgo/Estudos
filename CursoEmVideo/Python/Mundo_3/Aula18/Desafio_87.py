"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""
matriz = list([] for i in range(3))

for a in range(3):
    b = 0
    for b in range(3):
        while True:
            try: num = int(input("Digite um número"))
            except ValueError: print("Valor não reconhecido")
            else: break
        matriz[a].append(num)
print()

somapar = 0
for pos, i in enumerate(matriz):
    if pos != 0:
        print("\n")
    for n in i:
        if n % 2 == 0:
            somapar += n
        print(f"[ {n} ]",end="")


print(f"\nA soma dos pares é: {somapar}")
print(f"\nA soma da terceira coluna é: {sum(n[2] for n in matriz)}")
print(f"\nO maior número da segunda linha é: {max(matriz[1])}")