"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores
pares e os valores ímpares digitados, respectivamente
Ao final, mostre o conteúdo das três listas geradas.
"""
lista = []

while True:
    while True:
        try:
            num = int(input("Que número será colocado na lista?"))
            lista.append(num)
        except ValueError:
                print("\nValor não reconhecido\n")
        else: break
    while True:
        while True:
            try:
                condicao = input("Deseja continuar? (S/N): ").strip().upper()[0]
            except IndexError: print("Valor desconhecido")
            else: break
        if condicao not in "SN": print("Opção Inválida")
        else: break
        
    if condicao == "N": break

pares = list(n for n in lista if n % 2 == 0)

impares = list(n for n in lista if n % 2 == 1)

print(f"""
A lista inteira é: {lista}
Seus pares são: {pares}
Seus ímpares são: {impares}
""")