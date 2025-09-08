# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunoes e mostre a ordem sorteada

from random import sample

n1 = input('Primeiro Aluno')
n2 = input('Segundo Aluno')
n3 = input('Terceiro Aluno')
n4 = input('Quarto Aluno')

alunos = [n1, n2, n3, n4]

escolhido = sample(alunos,k=4)

print('A ordem de apresentação será',escolhido)