# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros

tam = float(input('Digite o tamanho em metros'))

km = tam/1000
hm = tam/100
dam = tam/10
dm = tam*10
cm = tam*100
mm = tam*1000

print('De acordo com o tamanho de {} metros,obtêm-se\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm'
      .format(tam,km,hm,dam,dm,cm,mm))