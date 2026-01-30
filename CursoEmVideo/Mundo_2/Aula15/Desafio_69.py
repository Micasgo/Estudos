"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar;
No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""
cont = mais18 = homens = mulher20anos = 0

while True:
    cont += 1
    print("\n","-="*10)
    print(f"Pessoa {cont}")
    idade = int(input("Qual a idade?: ").strip())
    sexo = input("Qual o sexo (M/F)?: ").strip().upper()[0]
    while sexo not in "MF": sexo = input("Qual o sexo? (M/F): ").strip().upper()[0]
    if idade > 18: mais18 += 1
    if sexo == "M": homens += 1
    if sexo == "F" and idade < 20: mulher20anos += 1
    condicao = input("\nQuer Continuar? (S/N): ").strip().upper()[0]
    while condicao not in "SN": condicao = input("\nQuer Continuar? (S/N): ").strip().upper()[0]
    if condicao == "N": break
print("-="*10)
print(f"""
De {cont} pessoa(s)
{mais18} mais de 18 anos;
{homens} homem(s)
{mulher20anos} mulher(es) com menos de 20 anos
""")