# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo e mostre o comprimento da hipotenusa.
from math import hypot
print('Para calcular a hipotenusa do seu triângulo retângulo por favor digite a baixo')
co = float(input('O valor do cateto oposto:'))
ca = float(input('O valor do cateto adjacente:'))
h = (co**2 + ca**2)**(1/2)
print('Para cateto oposto {} e cateto adjacente {} a hipotenusa vale {:.2f}.'.format(co, ca, h))
h1 = hypot(co, ca)
print(h1)

