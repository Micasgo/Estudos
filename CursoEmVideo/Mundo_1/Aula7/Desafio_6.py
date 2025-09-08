# Crie um algoritmo que leia um número
# e mostre o seu dobro o triplo e raiz quadrada

num = int(input ('Escreva um número'))

n2 = num*2
n3 = num*3
sqrt_n = num**(1/2)

print('O número é {}\nseu dobro e triplo respectivamente: {}, {}\ne sua raiz quadrada{}'
      .format(num, n2, n3, sqrt_n))
