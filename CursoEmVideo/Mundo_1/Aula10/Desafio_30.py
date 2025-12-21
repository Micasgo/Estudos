# Crie um programa que leia um número inteiro
# e mostre na tela se ele é impar ou par 

num = int(input("Digite um número: "))

if num%2 == 0:
    print("O número",num,"é par")
else:
    print("O número {} é impar".format(num))
