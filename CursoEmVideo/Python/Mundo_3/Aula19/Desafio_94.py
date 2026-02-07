"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada
pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo.
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
"""
def perguntaPolar(pergunta=str, A=str, B=str):
    while True:
        try:
            while True:
                condicao = input(f"{pergunta} ({A.upper()}/{B.upper()}): ").strip().upper()[0]
                if condicao not in (A+B): print("\nOpção Inválida")
                else: break
        except IndexError: print("\nValor não reconhecido")
        else: break
    return condicao
cont = 0
grupo = []

while True:
    cont += 1
    print("-="*15,"\n",f"{cont}° pessoa\n")
    nome = input("Qual o nome?: ")
    sexo = perguntaPolar("Qual o sexo?","M","F")
    while True:
        try: idade = int(input("Qual a idade?: "))
        except ValueError: print("Valor não reconhecido")
        else: break
    pessoa = {"nome":nome,"sexo":sexo,"idade":idade}
    grupo.append(pessoa.copy())
    if perguntaPolar("Quer continuar?","S","N") == "N": break

print("-="*15)
print(f"Foram cadastradas {len(grupo)} pessoa(s)\n")

#Modo Entusiasta
for pos, p in enumerate(grupo):
    if pos == 0:
        soma = p["idade"]
        mulher = []
        acimamedia = []
    else: soma += p["idade"]
    
    if p["sexo"] == "F": mulher.append(p["nome"])
mediaIdade = (soma/len(grupo))//1
mulheres = mulher


"""
modo preguiça
mediaIdade = (sum(p["idade"] for p in grupo)/len(grupo))
mulheres = list(p["nome"] for p in grupo if p["sexo"] == "F")
acimamedia = list(p["nome"] for p in grupo if p["idade"] > mediaIdade)
"""

print(f"{mediaIdade} é a média de idade do grupo")
print(f"Há {mulheres} de mulher no grupo")
print(f"Acima da média")
for p in grupo:
    if p["idade"] > mediaIdade: print(p,"\n")

#print(f"Há {acimamedia} acima da média de idade")