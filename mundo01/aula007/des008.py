# Escreva um programa que leia um valor em metros e exiba o valor convertido em cm e mm.
print('Por favor, digite a sua altura em metros:')
h = float(input('Altura:'))
h1 = h * 10**2
h2 = h * 10**3
print('O equivalente em cm e em mm da sua altura é respectivamente {} e {}'.format(h1, h2))
