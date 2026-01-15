"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
Só que agora utilizando o laço for
"""

num = int(input("Qual o número para ser tabuado?: "))

print("-=-"*5)
for i in range(10):
    print(f"{num} * {i+1} = {num*(i+1)}".center(15))

print("-=-"*5)

