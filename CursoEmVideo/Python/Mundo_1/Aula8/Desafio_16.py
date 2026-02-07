# Crie um programa que leia um número Real qualquer pelo teclado e
# mostre na tela a sua porção inteira.

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {:.0f}'.format(num,num//1))

