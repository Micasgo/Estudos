"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre m matriz na tela, com m formação correta.
"""
while True:
    try: tamanho = int(input("Qual o tamanho da matriz?"))
    except ValueError: print("Valor não reconhecido")
    else: break

matriz = (list([] for i in range(tamanho)))

for a in range(tamanho):
    for b in range(tamanho):
        while True:
            try: num = int(input(f"Digite um número para {a+1}, {b+1}: "))
            except ValueError: print("Valor não reconhecido")
            else: break
        matriz[a].append(num)

for c in matriz:
    print("\n")
    for n in c:
        print(f"[ {n} ] ".center(7),end="")
print()

def det_matriz_1(m=list):
    determinante = int(m[0][0])
    return determinante

def det_matriz_2(m=list):
    determinante = int((m[0][0] * m[1][1]) - (m[0][1] * m[1][0]))
    return determinante

def det_matriz_3(m=list):
    determinante = int((m[0][0]*m[1][1]*m[2][2])+(m[0][1]*m[1][2]*m[2][0])+(m[0][2]*m[1][0]*m[2][1]) -
    ((m[0][2]*m[1][1]*m[2][0])+(m[0][1]*m[1][0]*m[2][2])+(m[0][0]*m[1][2]*m[2][1])))
    return determinante


if tamanho == 1:
    print(f"A determinante da matriz é {det_matriz_1(matriz)}")
elif tamanho == 2:
    print(f"A determinante da matriz é {det_matriz_2(matriz)}")
elif tamanho == 3:
    print(f"A determinante da matriz é {det_matriz_3(matriz)}")