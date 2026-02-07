#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7.00 por cada Km acima do limite.
import colorama

vel = int(input("Digite a velocidade do carro em Km/h: "))
if vel <= 80:
    print(colorama.Fore.GREEN + "Tudo normal")
else:
    print(colorama.Fore.RED + "Você ultrapassou o limite de", colorama.Style.BRIGHT + " 80Km/h", colorama.Style.NORMAL + "e será multado em R${}".format(int(vel-80)*7))
print(colorama.Style.RESET_ALL)