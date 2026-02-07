"""
Crie um programa que simule o funcionamento de um caixa eletrõnico.
No início, pergunte o usurário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
rs50 = rs20 = rs10 = rs1 = 0

valor = int(input("Quanto você irá sacar em R$?: "))
"""
rs50 = valor // 50
rs20 = (valor - (rs50 * 50)) // 20
rs10 = (valor - (rs50 * 50) - (rs20 * 20)) // 10
rs1 = (valor - (rs50 * 50) - (rs20 * 20) - (rs10 * 10))
"""

while True:
    if valor >= 50:
        rs50 += 1
        valor -= 50
    elif valor >= 20:
        rs20 += 1
        valor -= 20
    elif valor >= 10:
        rs10 += 1
        valor -= 10
    elif valor >= 1:
        rs1 += 1
        valor -= 1
    else: break

print(f"""
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
{rs50} nota(s) de R$50 emitida(s)
{rs20} nota(s) de R$20 emitida(s)
{rs10} nota(s) de R$10 emitida(s)
{rs1} nota(s) de R$01 emitida(s)
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""")
