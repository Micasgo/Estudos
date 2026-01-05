"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
"""
atividades = int(input("Quantas atividades foram feitas?: "))

lista = []

total = 0

for i in range(atividades):
    nota = float((input(f"Qual foi a {i+1}° nota do aluno? :")).replace(",","."))
    lista.append(nota)

for i in range(len(lista)):
    total += float(lista[i])

media = total/len(lista)

if media < 5:
    print(f"Média final, {media:.2f}:\033[;31m REPROVADO\033[m")
elif media >= 5 and media < 7:
    print (f"Média final, {media:.2f}: \033[;33m RECUPERAÇÃO\033[m")
elif media >= 7 and media <= 10:
    print (f"Média final, {media:.2f}: \033[;32m APROVADO\033[m")
else:
    print (f"Média final, 10:\033[;32m APROVADO\033[m")
