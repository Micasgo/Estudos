# Faça um algoritmo que leia o salátio de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salario = float(input('Diga o valor em R$ do seu salário: R$ '))
aumento = int(input('Qual o número da porcentagem do aumento efetuado? : '))

vlrAmnt = salario*aumento/100
nsalario = salario+vlrAmnt

print('Com o valor de R${}, com um aumento de {}%, obterá um novo salário de R${:.2f}\nR${:.2f} de aumento'
      .format(salario,aumento,nsalario,vlrAmnt))
