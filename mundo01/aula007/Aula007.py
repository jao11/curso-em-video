# AULA 007
# Operadores Aritmeticos
# + adição
# - subtração
# * multiplicação
# / divisão
# ** potência ( pow(3,2)=9 isso é a função interna de potência que é outra maneira de resolver)
# // divisão inteira
# % modulo é o resto da divisão
# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1
# Ordem de precedência ( diz qual informação vai ser lida primeiro)
# 1º: ()
# 2º: **
# 3º: * / // %
# 4º: + -
# 5 + 3 * 2 == 11
# 3 * 5 + 4 ** 2 == 31
# 3 * (5 + 4) ** 2 == 243
nome = input('Qual é o seu nome?')
# repetição de caracter {:20}
print('Prazer em te conhecer {:20}!'.format(nome))  # adiciona( escreve o nome em) 20 espaços
print('Prazer em te conhecer {:<20}!'.format(nome))  # adiciona( escreve o nome em) 20 espaços a direita
print('Prazer em te conhecer {:>20}!'.format(nome))  # adiciona( escreve o nome em)20 espaços a esquerda
print('Prazer em te conhecer {:=<20}!'.format(nome))  # adiciona( escreve o nome em) 20  iguais a direita
print('Prazer em te conhecer {:^20}!'.format(nome))  # adiciona( escreve o nome em) 20 espaços centralizando o nome

n1 = int(input('Um valor'))
n2 = int(input('Outro valor'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(' A soma é {}, o produto é {} e a divisão é {:.3f}. '.format(s, m, d), end='')
print('A divisão inteira {} e potência {}.'.format(di, e))
print(' A soma é {}\n o produto é {}\n a divisão é {:.3f} '.format(s, m, d))
# Para controlar o número de decimais fazemos {:.3f} como colocamos o 3 temos três casas decimais
# Para quebrar a linha na resposta colocamos \n
# Para não quebrar( escrever em baixo) a linha da resposta colocamos ,end=''
# e só funciona para o print diretamente abaixo

print('A soma vale {}.'.format(n1+n2))