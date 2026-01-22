"""
Crie um programa que leia dois valores e mostre um menu na tela
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep

n1 = float(input("Digite o primeiro número: ").strip().replace(",","."))
n2 = float(input("Digite o segundo número: ").strip().replace(",","."))

opcao = "0"

while opcao != "5":
    print(f"""
Seus números são: {n1} e {n2}

[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
""")
    opcao = input("Qual opção você escolhe?: ")

    if opcao == "1":
        print(f"A soma é {n1+n2}")
    elif opcao == "2":
        print(f"A multiplicação é {n1*n2}")
    elif opcao == "3":
        print(f"O maior número é {max(n1,n2)}")
    elif opcao == "4":
        n1 = float(input("Digite o primeiro número: ").strip().replace(",","."))
        n2 = float(input("Digite o segundo número: ").strip().replace(",","."))
    elif opcao == "5":
        print("Adeus!")
    else:
        print("Opção não reconhecida, tente novamente\n","-="*25,"\n")
    sleep(1)
