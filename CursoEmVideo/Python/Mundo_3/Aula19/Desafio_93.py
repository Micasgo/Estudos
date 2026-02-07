"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols durante o campeonato
"""
def perguntaSN(pergunta = str):
    while True:
        try:
            while True:
                condicao = input(f"{pergunta} (S/N): ").strip().upper()[0]
                if condicao not in "SN": print("\nOpção Inválida")
                else: break
        except IndexError: print("\nValor não reconhecido")
        else: break
    return condicao

time = []
while True:
    nome = input("Qual o nome do jogador?: ")
    while True:
        try: numpart = int(input(f"Quantas partidas {nome} jogou?: "))
        except ValueError: print("Valor não reconhecido")
        else: break 
    gols = list(int(input(f"Quantos gols ele fez na {i+1}° partida")) for i in range(numpart))
    total = sum(gols)

    jogador = {"nome":nome,"numpart":numpart,"gols":gols,"total":total}
    time.append(jogador.copy())
    if perguntaSN("Deseja Continuar") == "N": break

for j in time:
    print("\n","-="*15,"\n",j,"\n")
    for c, v in j.items():
        print(f"O campo {c} recebeu {v}")
    print("-="*15,"\n")
    for pos, g in enumerate(j["gols"]):
        print(f"O jogador {j['nome']} fez {g} gol(s) na {pos+1}° partida")
