# Crie um programa que leia um número Real qualquer pelo teclado e
# mostre na tela a sua porção inteira.

import math

num = float(input('Diga o número'))

print ('O número {} tem sua parte inteira {}'.format(num,math.floor(num)))