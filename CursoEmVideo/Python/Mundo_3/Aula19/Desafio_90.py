"""
Faça um programa que leia o nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
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

sala = []
cont = 0

while True:
    cont += 1
    print(f"{cont}° Aluno")
    nome = input("Qual o nome?")
    media = int(input("Qual a média?"))
    if media < 6: situacao = "\033[;31mReprovado\033[m"
    else: situacao = "\033[;32mAprovado\033[m"
    aluno = {"nome": nome,"média": media, "situação":situacao}
    sala.append(aluno.copy())
    if perguntaSN("Quer continuar?") == "N": break

print(sala)
print("\n")
for pos, a in enumerate(sala):
    for c, v in a.items():
        print(f"No {pos+1}° dicionário, {c} = {v}")
