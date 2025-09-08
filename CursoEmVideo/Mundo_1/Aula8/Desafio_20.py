# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunoes e mostre a ordem sorteada
import random

n1 = input('Digite um nome')
n2 = input('Digite um nome')
n3 = input('Digite um nome')
n4 = input('Digite um nome')

alunos = [n1, n2, n3, n4]

cabeca = random.shuffle(alunos)

print ('A ordem de apresentação será {}'.format(alunos))