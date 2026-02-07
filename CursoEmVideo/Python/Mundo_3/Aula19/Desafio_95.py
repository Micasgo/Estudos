"""
Aprimore o Desafio_93 para que funcione com vários jogadores
inculindo um sistema de visualização de detalhes do aproveitamento de cada jogador
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

print("-="*15,"\n")
print(f"Num|Jogador      |Gols               |Total")

for pos, j in enumerate(time):
    print(f"{pos+1}   {j['nome'].ljust(14)}{str(j["gols"]):<20}{j["total"]}")

while perguntaSN("Quer o detalhamento de um jogador?") == "S":
    try:
        while True:
            try: escolha = int(input("Qual o número do jogador a ser selecionado?"))
            except ValueError: print("Valor não reconhecido")
            else: break
        print("-="*15)
        print(f"\nLevantamento de {time[escolha-1]["nome"]}")
        for jogo, g in enumerate(time[escolha-1]["gols"]):
            print(f"Na {jogo+1}° partida, fez {g} gol(s)")
    except IndexError: print("Opção Inválida")
print("Encerrando...")
