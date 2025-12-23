"""
    Desenvolva um programa que leia o comprimento de três retas e
    diga ao usuário se elas podem ou não formar um triângulo
"""

a = float(input("Digite o comprimento do primeiro lado do triângulo. : ").strip().replace(",","."))
b = float(input("Digite o comprimento do segundo lado. : ").strip().replace(",","."))
c = float(input("Digite o comprimento do terceiro lado. : ").strip().replace(",","."))

if (
    a + b > c and
    a + c > b and
    b + c > a
):

    print("O triângulo com os lados",a,b,c,"pode ser formado")

else:

    if (a + b > c) == False:
        motivo = (f"porque {a} + {b} não é maior que {c}")

    if (a + c > b) == False:
        motivo = (f"porque {a} + {c} não é maior que {b}")

    if (b + c > a) == False:
        motivo = (f"porque {b} + {c} não é maior que {a}")

    print("O triângulo não pode ser formado", motivo)

