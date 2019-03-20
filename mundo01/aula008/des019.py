# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um
# programa que leia o nome deles e escreva o nome do escolhido.
import random
print('Irei sortear um de vocês para decidir quem irá apagar o quadro. Por favor coloquem o nome abaixo:')
a1 = str(input('1º estudante:'))
a2 = str(input('2º estudante:'))
a3 = str(input('3º estudante:'))
a4 = str(input('4º estudante:'))
a = random.choice([a1, a2, a3, a4])  # O comando choice sorteia uma coisa do conjunto que foi apresentado
print('E o aluno sorteado é {}.'.format(a))
