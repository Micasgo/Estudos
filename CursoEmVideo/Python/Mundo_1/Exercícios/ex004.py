# Faça um programa que leia algo pelo teclado e mostre
# na tela seu tipo primitivo e todas as informações
# possiveis sobre ele

n = input('Escreve algo pra poder ver coisas magníficas')

print('O tipo primitivo de {} é'.format(n), type(n))
print(n, 'é alfabético?',n.isalpha())
print(n, 'é numérico?', n.isnumeric())
print(n, 'é somente espaços?', n.isspace())
print(n, 'está em maiúsculas?', n.isupper())
print(n, 'Está em minúsculas?', n.islower())
print(n, 'Está capitalizada?', n.istitle())
