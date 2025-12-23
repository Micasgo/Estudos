# Crie um programa que leia um número inteiro
# e mostre na tela se ele é impar ou par 

import colorama

num = int(input("Digite um número: "))

if num%2 == 0:
    print("O número",num, "é",colorama.Fore.CYAN + "par")

else:
    print("O número {} é" ,colorama.Fore.RED + "impar".format(num))
colorama.Fore.RESET
