# Faça um programa que leia um ângulo qualquer e  mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input('Digite o ângulo desejado'))


seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('Para o ângulo de {} graus\nSeno é igual a {:.2f}\nCosseno é igual a {:.2f}\nTangente é igual a {:.2f}'
      .format(ang,seno,cosseno,tangente))