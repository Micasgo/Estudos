# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

dist = float(input('Qual é o tamanho em metros?'))

cm = dist*100
mm = dist*1000

print('{} metros é igual a {:.2f} centímetros ou {:.2f} milímetros'.format((dist),(cm),(mm)))
