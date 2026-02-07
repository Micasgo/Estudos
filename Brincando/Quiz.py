quiz = int(input("Quantas questões você quer colocar?: "))
dicionarios = []
letras = ("A","B","C","D","E")
pontuacao = 0

for i in range(quiz):
    pergunta = input(f"Qual a pergunta para a {i+1}° questão: ")
    lista = list(input(f"Qual a {n+1}° resposta para a pergunta?: ")for n in range(5))
    while True:
        resposta = int(input("Qual dessas respostas é a certa? (1,2,3,4 ou 5): ").strip())
        if not 1 <= resposta <= 5: print("Opção Inválida, escreva novamente")
        else: break
    dicionarios.append({'pergunta': pergunta,'alternativas':lista,"resposta":resposta-1})

print(f"\n"*5,f"{"QUIZ":^25}\n\n")
for pos, p in enumerate(dicionarios):
    print(f"{pos+1}° Questão\n")
    print(f"{p["pergunta"]}")
    for letra, o in enumerate(p["alternativas"]):
        print(f"{letras[letra]}) {o}")
    while True:
        marcado = input("Qual a resposta certa? (A, B, C, D ou E): ").strip().upper()
        if marcado not in "ABCDE": print("Opção Inválida, escreva novamente")
        else: break
    if letras.index(marcado) == p["resposta"]:
        pontuacao += 1
    print()

print(f"Você marcou {pontuacao} pontos de {len(dicionarios)}\n")
print(f"{(pontuacao/len(dicionarios))*100:.0f}% de aproveitamento!")