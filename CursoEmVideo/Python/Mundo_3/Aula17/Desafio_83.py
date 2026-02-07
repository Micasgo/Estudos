"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.
"""

contador = 0

while True:
    formula = input("Qual equação a ser verificada?: ")
    if "(" not in formula and ")" not in formula:
        print("Essa equação não precisa ser verificada")
    else: break

for c in formula:
    if c == "(":
        contador += 1
    elif c == ")":
        contador -= 1
    if contador < 0:
        print(f"Sua equação está \033[;31merrada!\033[m")
        break
if contador >= 0:
    if contador == 0: print(f"Sua equação está \033[;32mcorreta\033[m!")
    else: print(f"Sua equação está \033[;31merrada!\033[m")
