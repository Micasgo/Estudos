"""
Crie um programa que tenha uma função fatorial() que receba dois parãmetros:
o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""

def fatorial(num, show = False):
    fatorial = 1
    if show:
        from time import sleep
        for i in range (num,0,-1):
            fatorial *= i
            print(f"{i} * ",end="",flush=True)
            if i - 2 == 0:
                print("1 = {}".format(fatorial),end="",flush=True)
                sleep(0.2)
                break
            sleep(0.2)
    else:
        for i in range (num,0,-1):
            fatorial *= i
    return fatorial

fatorial(6, show = True)