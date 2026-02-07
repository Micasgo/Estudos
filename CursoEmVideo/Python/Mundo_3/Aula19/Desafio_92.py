"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-se (com idade)
em um dicionário, se por acaso a CTPS for diferente de 0,
o dicionário receberá também o ano de contratação.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
"""
def perguntaSN(pergunta=str):
    while True:
        try:
            while True:
                condicao = input(f"{pergunta} (S/N): ").strip().upper()[0]
                if condicao not in "SN": print("Opção Inválida")
                else: break
        except IndexError: print("Valor não reconhecido")
        else: break
    return condicao
from datetime import datetime
anoatual = datetime.today().year

grupo = []

while True:
    nome = input("\nQual o seu nome?: ")
    while True:
        try: nasc = int(input("\nQual seu ano de nascimento?: "))
        except ValueError: print("\nValor não reconhecido")
        else: break
    while True:
        try: ctps = int(input("\nQual o número da sua carteira de trabalho?"))
        except ValueError: print("\nValor não reconhecido")
        else: break
    if ctps != 0:
        while True:
            try: anocontr = int(input("Qual o ano de contratação da sua CTPS?: "))
            except ValueError: print("\nValor não reconhecido")
            else: break
        pessoa = {"nome":nome,"nasc":nasc,"ctps":ctps,"anocontr":anocontr}
    else:
        pessoa = {"nome":nome,"nasc":nasc,"ctps":ctps}
    grupo.append(pessoa.copy())
    if perguntaSN("Quer continuar?") == "N":
        break

for p in grupo:
    idade = anoatual - p["nasc"]
    print("\n","-="*15)
    print(f"A idade de {p["nome"]} é {idade}",end="")
    if p["ctps"] == 0:
        print("\nNão há valores de trabalho envolvendo essa pessoa")
    else:
        trabalhofalt = 15 - (anoatual-p["anocontr"])
        if trabalhofalt <0: trabalhofalt = 0
        aposentadoria = idade + trabalhofalt
        print(f" e se aposentará com {aposentadoria}\n")
