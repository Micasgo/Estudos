"""
Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente
"""
def intinput(pergunta=str):
    while True:
        try:valor = int(input(f"{pergunta}: "))
        except ValueError:
            print("\nValor não reconhecido")
            return 0
        else: break
    return valor

def ficha(nome = "\033[4;31mREDACTED\033[m", gols = 0):
    if nome == "": nome = "\033[4;31mREDACTED\033[m"
    print(f"O jogador {nome} marcou {gols} gol(s)")

nome = input("Qual o nome do jogador?: ").strip()
gols = intinput("Quantos gols ele fez?")

ficha(nome=nome, gols=gols)

