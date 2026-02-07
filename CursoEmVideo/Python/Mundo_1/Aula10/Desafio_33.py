
'''
    Faça um programa que leia três números e
    mostre qual é o maior e qual é o menor
'''

'''
num1 = int(input("Digite o primeiro número :"))
num2 = int(input("Digite o segundo número :"))
num3 = int(input("Digite o terceiro número :"))

if num1 > num2 and num1 > num3:
    print("O número", num1, "é o maior")
if num2 > num1 and num2 > num3:
    print("O número", num2,"é o maior")
if num3 > num1 and num3 > num2:
    print("O número", num3,"é o maior")
if num1 < num2 and num1 < num3:
    print("O número", num1, "é o menor")
if num2 < num1 and num2 < num3:
    print("O número", num2,"é o menor")
if num3 < num1 and num3 < num2:
    print("O número", num3,"é o menor")
if num1 == num2:
    print("O primeiro e segundo números são iguais")
if num2 == num3:
    print("O segundo e terceiro números são iguais")
if num1 == num3:
    print("O primeiro e terceiro números são iguais")
if num1 == num2 == num3:
    print("Todos os números são iguais")
'''


num = []
for i in range (3):
    n = int(input("Digite o {}° número".format(i+1)))
    num.append(n)

num.sort()

print("O menor número é",num[0])
print("O maior número é", num[-1])
