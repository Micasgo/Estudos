"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua tvida:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""

import datetime

hoje = datetime.date.today()



ano = int(input("Qual o ano do seu nascimento?"))
mes = int(input("Qual o mês do seu nascimento? (em número)"))
dia = int(input("Qual o dia do seu nascimento?"))

nascimento = datetime.date(ano,mes,dia)

tvida = (hoje - nascimento).days

idade = tvida//365
mesv = (tvida%365)//30
diav = (tvida%365)%30

if mesv == 0:
    mesv +=1

if diav == 0:
    mesv +=1


ftvida = datetime.date(idade, mesv, diav)


if idade < 18:
    print(f"Você precisará esperar {17-idade} anos e {13-hoje.month-mesv} meses para se alistar")
    
elif idade == 18:
    print(f"Você está no momento certo de se alistar!")
elif idade > 18:
    print(f"Você passou do tempo em se alistar em {idade-18} anos {mesv} meses")
