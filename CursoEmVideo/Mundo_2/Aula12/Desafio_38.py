"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

num1 = int(input("Digite um número para comparar: "))
num2 = int(input("Digite outro número para a comparação: "))

if num1 > num2:
    print(f"O primeiro número ({num1}) é maior que o segundo ({num2})")
elif num2 > num1:
    print(f"O segundo número ({num2}) é maior que o primeiro ({num1})")
else:
    print(f"Não existe valor maior, os dois são iguais",num2)