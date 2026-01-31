"""
Desenvolva um programa que leia quatro valores pelo teclado e guade-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""
vezes9 = 0

tupla = tuple(int(input("Digite um número"))for i in range(4))

print(f"\n{tupla.count(9)} é o total de algarismos 9 dentro da tupla")

try:
    index3 = tupla.index(3)
except ValueError:
    print("\nNão há o número 3 na tupla")
else:
    print(f"\n{index3} é o índice do primeiro 3 digitado")

pares = list(str(n) for n in tupla if n % 2 == 0)

print(f"\nÉ/são os pares da tupla: {", ".join(pares)}\n")


#print(f"\n{list(pos for pos, n in enumerate(tupla) if n == 3)[0]} é o índice do primeiro 3 digitado")
