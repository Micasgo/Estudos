"""
Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e
permita que o usuário possa mostrar as notas de cada aluno individualmente
"""
def perguntaSN(pergunta=str):
    while True:
        try:
            while True:
                condicao = input(f"\n{pergunta} (S/N): ").strip().upper()[0]
                if condicao not in "SN": print("\nOpção Inválida")
                else: break
        except IndexError: print("\nValor não reconhecido")
        else: break
    return condicao

cont = 0
sala = []

while True:
    print(f"{cont+1}° Aluno".center(20),"\n","-="*10)
    nome = input("\nQual o nome do aluno?: ")
    while True:
        try:
            nt1 = float(input("Qual a 1° nota do aluno?: ").replace(",","."))
            nt2 = float(input("Qual a 2° nota do aluno?: ").replace(",","."))
        except ValueError: print("\nValor não reconhecido\n")
        else: break

    condicao = perguntaSN("Quer continuar?")

    aluno = [nome,nt1,nt2]
    sala.append(aluno[:])
    aluno.clear()
    cont += 1
    if condicao == "N": break

sala.sort()
for pos, i in enumerate(sala):
    media = (i[1]+i[2])/2
    print(f"{pos+1} - {i[0]:.<30}", f"{media:.1f}")

while True:
    condicao = perguntaSN("Quer ver as notas individuais de algum aluno?")
    if condicao == "S":
        while True:
            try:
                while True:
                    try:
                        num = int(input("Qual o número do aluno?")) - 1
                    except ValueError: print("Valor não reconhecido")
                    else: break
                print(f"As notas de {sala[num][0]} foram: {sala[num][1]} e {sala[num][2]}")
            except IndexError: print("\nOpção Inválida")
            else: break
    else: break
    