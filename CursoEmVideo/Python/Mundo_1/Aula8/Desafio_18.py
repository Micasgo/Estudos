# Faça um programa que leia um ângulo qualquer e  mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

import math

ang = int(input('Digite o valor do ângulo'))

ang_degree = math.radians(ang)

print('Para {} graus\nO seno é {:.2f}\nO cosseno é {:.2f}\nE a tangente é {:.2f}'
      .format(ang, math.sin(ang_degree), math.cos(ang_degree), math.tan(ang_degree)))