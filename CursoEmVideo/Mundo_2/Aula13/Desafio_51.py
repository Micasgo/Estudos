"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

a1 = int(input("Digite o primeiro termo da P.A.\n\n:"))

r = int(input("Digite a razão da P.A.\n\n:"))

pa = int(input("Qual o tamanho da P.A. requerida?\n\n:"))

lista = []

for i in range(pa):
    lista.append(str(a1+(i*r)))
    
print(", ".join(lista))
