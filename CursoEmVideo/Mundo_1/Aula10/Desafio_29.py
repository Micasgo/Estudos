#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7.00 por cada Km acima do limite.

vel = int(input("Digite a velocidade do carro em Km/h: "))
if vel <= 80:
    print("Tudo normal")
else:
    print("Você será multado em R${}".format(int(vel-80)*7))