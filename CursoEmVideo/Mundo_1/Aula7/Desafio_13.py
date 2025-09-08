# Faça um algoritmo que leia o salátio de um funcionário
# e mostre seu novo salário, com 15% de aumento

slr = float(input('Digite o salário.'))
amnt = int(input('Digite o número do aumento em porcentagem'))
amntB = slr*amnt/100
slrA = slr+amntB

print('Com o salário de {} reais, com {}% de aumento, fica {:.2f}, um aumento de {:.2f}'.
      format(slr,amnt,slrA, amntB))
