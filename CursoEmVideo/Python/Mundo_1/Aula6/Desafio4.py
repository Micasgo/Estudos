# Faça um programa que leia algo pelo teclado e mostre
# na tela seu tipo primitivo e todas as informações
# possiveis sobre ele

n = input('Escreve aí um negócio pa eu ver')

'''
print(n, "para número é", n.isnumeric(),
      "para letra é", n.isalpha(),
      "para minúsculo é", n.islower(),
      "para maiúsculo é", n.isupper(),
      "para alfanumérico é", n.isalnum())
      '''

print(n, "para número é", n.isnumeric())
print(n, "para letra é", n.isalpha())
print(n, "para minúsculo é", n.islower())
print(n, "para maiúsculo é", n.isupper())
print(n, "para alfanumérico é", n.isalnum())