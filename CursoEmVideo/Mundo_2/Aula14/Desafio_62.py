"""
Melhore o Desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos
"""

a1 = int(input("Qual o primeiro termo da P.A.?: "))
r = int(input("Qual a razão da P.A.?: "))
pa = int(input("Qual o tamanho da P.A.?: "))
termo1 = a1
lista = []
final = []

while termo1 != a1 + (r*(pa-1)):
    lista.append(str(termo1))
    termo1 += r
lista.append(str(termo1))

print(f"Sua P.A. é: {", ".join(lista)}")

final.extend(lista)
lista.clear()

opcao = int(input("Quer que mais termos sejam mostrados? (Digite um número diferente de 0 para continuar): "))

termo2 = termo1

while opcao != 0:
    while termo1 != termo2 + (r*opcao):
        termo1 += r
        lista.append(str(termo1))
    print(f"A continuação é: {", ".join(lista)}\n")
    final.extend(lista)
    lista.clear()
    opcao = int(input("Quer que mais termos sejam mostrados? (Digite um número diferente de 0 para continuar): "))
    termo2 = termo1

print(f"No fim sua P.A. ficou com {len(final)} termos: {", ".join(final)}")
