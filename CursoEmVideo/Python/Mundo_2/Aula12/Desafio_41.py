"""
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categora, de acordo com a idade:
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
"""

from datetime import date

ano = int(input("Qual o ano de nascimento?: "))
mes = int(input("Qual o mês de nascimento?: "))
dia = int(input("Qual o dia do nascimento?: "))

data = str(date.today())

anoAtual = int(data[:4])
mesAtual = int(data[5:7])
diaAtual = int(data[8:10])

idade = anoAtual - ano


if mes > mesAtual:
        idade -=1
elif mes <= mesAtual and dia > diaAtual:
        idade -=1


if idade <= 9:
    print(f"Com {idade} anos, foi qualificado para Categoria Mirim")

elif idade > 9 and idade <= 14:
    print(f"Com {idade} anos, foi qualificado para Categoria Infantil")

elif idade > 14 and idade <= 19:
    print(f"Com {idade} anos, foi qualificado para Categoria Junior")

elif idade == 20:
    print(f"Com {idade} anos, foi qualificado para Categoria Sênior")

elif idade > 20:
    print(f"Com {idade} anos, foi qualificado para Categoria Master")
