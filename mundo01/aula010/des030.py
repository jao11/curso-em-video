'''

Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

'''



n = int(input('Digite um número inteiro:'))

n1 = n % 2

if n1 == 0:      # != é o símbolo de diferente

    print('Seu número é par.')

else:

    print('Seu número é impar.')
