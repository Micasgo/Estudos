"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.
"""

def notas(*notas, sit: bool | None = False):
    """
    Recebe notas e exibe a quantidade de notas, a maior, menor , média e situação.
    
    :param notas: Recebe as notas
    :param sit: Faz aparecer com um print a situação das notas
    """
    for pos, n in enumerate(notas):
        if pos == 0:
            soma = n
            maior = n
            menor = n
        else:
            soma += n
            if maior < n: maior = n
            if menor > n: menor = n
    media = soma/len(notas)
    if media < 6: situacao = "\033[;31mReprovado\033[m"
    elif 6 <= media <= 10: situacao = "\033[;32mAprovado\033[m"
    turma = {"num notas":len(notas),"maior nota": maior,"Menor nota":menor,"media":float(f"{media:.2f}")}
    if sit: turma["situacao"] = situacao
    print(turma)

notas(9.2,7,8.5,9.2,8.3,5.2,7.9,7,8.5,8.3,7.8,6.4,6.1)