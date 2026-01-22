"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
s = input("Qual o seu sexo? (M/F)")

while s not in "MF":
    print("Opção digitada incorretamente, digite M ou F")
    s = input("Qual o seu sexo? (M/F)")
if s == "M":
    print("Olá Macho")
elif s == "F":
    print("Olá Fêmea")
