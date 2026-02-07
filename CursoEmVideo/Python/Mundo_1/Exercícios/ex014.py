#Faça um programa que converta graus celsius para fahrenheit e vice-versa
# C = ( °F - 32 ) × 5/9
# F = ( °C × 9/5 ) + 32

var = input('Se você quer converter um valor de Fahrenheit para Celsius, digite C\nSe você quer converter um valor de Celsius para Fahrenheit, digite F\n')

if var=='C':
   fah = float(input('Digite o valor em Fahrenheit'))
   print('O valor de {} graus Fahrenheit equivale-se à {:.2f} graus Celsius'.format(fah,(fah-32)*5/9))
   quit()

if var =='F':
   cel = float(input('Digite o valor em Celsius'))
   print('O valor de {} graus Celsius, equivale-se à {:.2f} graus Fahrenheit'.format(cel,cel*9/5+32))

else:
   print('Você escreveu algo que não estava nas condições, digite F ou C para o requisitado, em maiúsculo')