"""
Fala um programa que leia um número inteiro e diga se ele é ou não um primo.
"""

num = int(input("Digite um número\n\n:"))

if num != 0:
    for i in range(0,num):

        if i >= 2:
            if num % i == 0:
                print(f"O número {num} não é primo")
                break


    if i == num-1:
        print(f"O número {num} é primo")
elif num == 0:
    print("É sério isso? Zero?")