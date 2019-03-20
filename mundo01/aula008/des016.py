# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua
# porção inteira.
# exemplo: digite um número 6.124 , o número 6.124 tem a parte inteira 6
from math import trunc
n = float(input('Por favor digite um número qualquer:'))
n1 = trunc(n)
print('A parte inteira de {} vale {}'.format(n, n1))
