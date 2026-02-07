"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números forma digitados e qual foi a soma entre eles (desconsiderando o flag)
"""
cont = sum = 0

num = int(input("Digite um número a ser somado (Digite 999 para parar): "))
while True:
    if num == 999: break
    cont +=1
    sum += num
    num = int(input("Digite um número a ser somado: "))

print(f"A soma dos {cont} números foi de: {sum}")
