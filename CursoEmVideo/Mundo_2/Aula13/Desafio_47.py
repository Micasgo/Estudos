"""
Crie um programa que mostre na tela todos os números que estão no intervalo entre 1 e 50
"""
alcance = int(input("Qual o alcance da medida?: "))

print(f"Todos os números pares entre 0 e {alcance} são:")

for i in range(alcance+1):
    if i % 2 == 0:
        print(f"{i}")
