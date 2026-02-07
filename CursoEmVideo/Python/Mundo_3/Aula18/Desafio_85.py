"""
Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""

nums = [[],[]]

for i in range(7):
    while True:
        try:
            num = int(input("Digite um número: "))
        except ValueError: print("Valor não reconhecido")
        else: break
    if num % 2 == 0: nums[1].append(num)
    elif num % 2 == 1: nums[0].append(num)
    
nums[0].sort()
nums[1].sort()

print(f"Os valores ímpares são {nums[0]}")
print(f"Os números pares são {nums[1]}")
