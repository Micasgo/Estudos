'''
nome = input('Qual o seu nome?')
print ('Seja bem vindo {:h^20}!'.format(nome))
'''

n1 = int(input('Um número'))
n2 = int(input('Outro valor aí'))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
exp = n1 ** n2
divInt = n1 // n2
divRes = n1 % n2

print('A soma é {}\no produto é {}\na divisão é {:.3f}'
      .format(soma, mult, div,), end=(' ==> '))
print('A divisão inteira é {} e o resto/módulo é {}'.format(divInt, divRes))
print('A exponenciação é {}'.format(exp))