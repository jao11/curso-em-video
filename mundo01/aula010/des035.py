'''

Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas

podem ou não formar um triângulo.

'''



print('Digite o tamanho das suas retas abaixo:')

r1 = float(input('reta 1:'))

r2 = float(input('reta 2:'))

r3 = float(input('reta 3:'))

g = r1 + r2

p = r1 - r2

if g > r3 > abs(p):

    print('Suas retas podem formar um triângulo.')

else:

    print('Sua retas não podem formar um triângulo.')
