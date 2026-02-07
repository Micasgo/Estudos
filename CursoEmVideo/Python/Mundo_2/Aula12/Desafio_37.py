"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão: 1 para binário, 2 para octal, 3 para hexadecimal
"""



numero = int(input("Digite o número a ser convertido: "))

escolha = int(input("Para converter o número para: \
\nBinário, digite 1 \
\nOctal, digite 2 \
\nHexadecimal, digite 3\n\n"))

lixo1 = str(bin(numero))[0:2]
lixo2 = str(oct(numero))[0:2]
lixo3 = str(hex(numero))[0:2]

if escolha == 1:
    print(f"O número {numero} em binário é {str(bin(numero)).replace(lixo1,"")}")
elif escolha == 2:
    print(f"O número {numero} em octal é {str(oct(numero)).replace(lixo2,"")}")
elif escolha == 3:
    print(f"O número {numero} em hexadecimal é {str(hex(numero)).replace(lixo3,"")}")
else:
    print("Opção inválida")