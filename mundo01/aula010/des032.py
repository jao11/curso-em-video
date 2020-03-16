'''

Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

'''



n = int(input('Digite um ano qualquer:'))

n1 = n % 4

if n1 == 0:      # != é o símbolo de diferente

    print('Seu ano é bissexto.')

else:

    print('Seu ano não é bissexto.')
