# Escreva um programa que pergunte  a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

dias = int(input('Quantos dias o carro ficou alugado? :'))
km = int(input('Quantos quilômetros o carro alugado percorreu? :'))

valor = 60*dias + 0.15*km

print ('Com um carro alugado a {} dias e tendo rodado {}km, o valor a ser pago será de R${:.2f}.'
       .format(dias,km,valor))