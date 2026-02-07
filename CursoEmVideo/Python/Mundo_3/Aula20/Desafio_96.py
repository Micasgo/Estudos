"""
Faça um programa que tenha uma função chamada àrea(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a àrea do terreno.
"""

def area(largura=int,comprimento=int):
    area = largura*comprimento
    print(f"A área do polígono regular é com largura {largura} e comprimento {comprimento} é: \033[;32m{area}\033[m u.m²")
def intinput(pergunta=str):
    while True:
        try:valor = int(input(f"{pergunta}: "))
        except ValueError: print("\nValor não reconhecido")
        else: break
    return valor


larg = intinput("Qual a largura do polígono regular?")
print()
comp = intinput("Qual o comprimento do polígono regular?")
print()

area(larg,comp)