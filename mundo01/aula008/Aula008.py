# AULA 008
# Trabalhando com módulos
# Para inluir(importar) algo usa-se o comando import
# 'import( biblioteca)' comando geral
# Para importar somente uma parte escrevemos
# 'from(biblioteca)import(item específico)' comando específico
# Bibliotecas básicas: math
# Exemplo
import math

# from math import sqrt
num = int(input('digite um número:'))
# raiz = sqrt(num)
raiz = math.sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, raiz))
print('A raiz de {} é {}'.format(num, math.ceil(raiz)))  # ceil = arredondar para cima
print('A raiz de {} é {}'.format(num, math.floor(raiz)))  # floor = arredondar para baixo
print('A raiz de {} é {}'.format(num, math.trunc(raiz)))  # trunc = quebra o número
import random  # A biblioteca random gera um número aleatório entre 0 e 1

num1 = random.random()
num2 = random.randint(1, 10)
print(num1)
print(num2)
import emoji  # Para importar novas bibliotecas clicar na lâmpada vermelha e adicionar

print(emoji.emojize('Olá mundo :imp:', use_aliases=True))
print(emoji.emojize('Olá mundo:earth_americas:', use_aliases=True))
