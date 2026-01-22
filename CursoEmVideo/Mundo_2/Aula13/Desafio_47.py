"""
Crie um programa que mostre na tela todos os números que estão no intervalo entre 1 e 50
"""
alcance = int(input("Qual o alcance da medida?: "))

print(f"Todos os números pares entre 0 e {alcance} são:")

for i in range(0, alcance+1,2):

    print(f"{i}")