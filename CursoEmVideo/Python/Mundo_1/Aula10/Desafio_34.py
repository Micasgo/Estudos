'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1250,00 calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%.
'''


sal = float((input("Qual o seu salário? :").strip().replace(",",".")))

if sal > 1250:
    print(f"Seu salário de R${sal} terá um aumento de 10%, equivalente à R${sal*0.1:.2f}, acumulando um total de R${sal*1.1:.2f}")
else:
    print(f"Seu salário de R${sal} terá um aumento de 15%, equivalente à R${sal*0.15:.2f}, acumulando um total de R${sal*1.15:.2f}")
