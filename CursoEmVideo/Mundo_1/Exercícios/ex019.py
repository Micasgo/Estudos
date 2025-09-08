# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

n1 = input('Primeiro Aluno')
n2 = input('Segundo Aluno')
n3 = input('Terceiro Aluno')
n4 = input('Quarto Aluno')

alunos = [n1, n2, n3, n4]

print(choice(alunos))