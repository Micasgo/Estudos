#Faça um programa que leia o comprimento do cateto oposto 
# do cateto adjacente de um triângulo, calcula e mostra o 
# comprimento da hipotenusa

from math import (sqrt,pow)

cata = float(input('Digite o valor do cateto adjacente :'))
cato = float(input('Digite o valor do cateto oposto :'))

hipo = sqrt(pow(cata,2) + pow(cato,2))

print('O valor da hipotenusa é {:.2f}'.format(hipo))
