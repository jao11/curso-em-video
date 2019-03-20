# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do o seno
# o cosseno e a tangente desse ângulo.
import math
a = float(input('Por favor informe um ângulo qualquer:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O seno, o cosseno e a tangente do ângulo informado são respectivamente:\n {:.2f}, {:.2f}, {:.2f}.'.format(s, c, t))
