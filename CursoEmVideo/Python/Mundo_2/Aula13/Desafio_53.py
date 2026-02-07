"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

frase = input("Digite a frase: ").replace(" ","").lower()
fraseR = frase[::-1]

if frase == fraseR:
    print("Sua frase é um palíndromo")
else:
    print("Sua frase não é um palíndromo")
