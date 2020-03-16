'''

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

'''



print('Por favor digite três números abaixo.')

n1 = float(input('primeiro número:'))

n2 = float(input('Segundo número:'))

n3 = float(input('Terceiro número:'))

if n1 > n3 > n2:

    print('O {} é o maior e o {} é o menor'.format(n1, n2))

elif n3 > n2 > n1:

    print('O {} é o maior e o {} é o menor'.format(n3, n1))

elif n2 > n1 > n3:

    print('O {} é o maior e o {} é o menor'.format(n2, n3))

elif n2 > n3 > n1:

    print('O {} é o maior e o {} é o menor'.format(n2, n1))

elif n1 > n2 > n3:

    print('O {} é o maior e o {} é o menor'.format(n1, n3))

else:

    print('O {} é o maior e o {} é o menor'.format(n3, n2))
