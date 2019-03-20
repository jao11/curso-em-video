# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
# sorteada.
from random import shuffle

print('Para saber a ordem de apresentação por favor digite os seus nomes')
a1 = str(input('1º estudante:'))
a2 = str(input('2º estudante:'))
a3 = str(input('3º estudante:'))
a4 = str(input('4º estudante:'))
ordem = [a1, a2, a3, a4]
shuffle(ordem)  # O comando shuffle(significa embaralhar) sorteia uma
# ordenação para uma lista de coisas
print('A ordem de apresentação será:', ordem)
