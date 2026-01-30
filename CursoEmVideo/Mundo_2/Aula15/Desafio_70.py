"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual o nome do produto mais barato.
"""

maisde1000 = total = cont = 0


while True:
    cont += 1
    print(f"\nProduto {cont}")
    produto = input("Qual o nome do produto?: ")
    preco = float(input("Qual o valor do produto em R$? :").strip().replace(",","."))
    total += preco
    if preco > 1000: maisde1000 += 1
    if cont == 1:
        min = preco
        barato = produto
    if preco < min:
        min = preco
        barato = produto
    condicao = input("Quer continuar? (S/N): ").strip().upper()[0]
    if condicao == "N": break

print(f"""\n
O valor total da compra dos {cont} itens será de: \033[:32mR${total:.2f}\033[m
{maisde1000} produto(s) custa(m) mais de R$1000,00
O nome do produto mais barato é: {barato}
""")
