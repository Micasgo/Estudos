"""
Refaça o Desafio 35 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles dois lados iguais
- Escaleno: todos os lados diferentes
"""

a = float(input("Qual o comprimento do 1° lado?: ").replace(",","."))
b = float(input("Qual o comprimento do 2° lado?: ").replace(",","."))
c = float(input("Qual o comprimento do 3° lado?: ").replace(",","."))

if (
    a + b > c and
    a + c > b and
    b + c > a
):
    print("É possível fazer um triângulo com esses lados\n")

    if a == b == c:
        print("Você fará um triângulo Equilátero")
    elif a == b or b == c or a == c:
        print("Você fará um triângulo Isósceles")
    else:
        print("Você fará um triângulo escaleno")
else:
    print("Não é possível criar um triângulo com esses lados")
