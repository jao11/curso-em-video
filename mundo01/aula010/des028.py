'''

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e

peça para o usuário tentar descobrir qual número foi escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''

from random import randint



n = randint(1, 6)

n1 = int(input('Pensei em um número de 0 à 5 e quero que você tente adivinhar qual é,'

               ' para isso digite\num número a seguir:'))

if n == n1:

    print('Parabéns você acertou o número que eu pensei.')

else:

    print('Sinto muito você errou o meu número.\n'

          'O meu número era o {}.'.format(n))
