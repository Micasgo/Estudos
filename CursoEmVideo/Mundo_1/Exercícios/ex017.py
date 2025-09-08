#Faça um programa que leia o comprimento do cateto oposto 
# do cateto adjacente de um triângulo, calcula e mostra o 
# comprimento da hipotenusa

ca = float(input("Qual o Cateto Adjascente? :"))
co = float(input('Qual o Cateto Oposto? :'))
hipo = (ca**2+co**2)**0.5

print('Com o cateto adjascente {} e o oposto {}, a hipotenusa é {:.2f}'.format(ca,co,hipo))

