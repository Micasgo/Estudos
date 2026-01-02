class cores:
    normal = 0
    negrito = 1
    vermelho = f'\033[0;31m'
    verde = f'\033[0;32m'
    reset = '\033[m'
    
def criar_aviso(texto=str, estilo=cores.normal, cor=cores.vermelho):
   
    print(f"{f'{cor}'.replace("0",str(estilo))}{texto}{cores.reset}")

criar_aviso("Eu sou burro",cores.normal,cores.vermelho)