'''

Escreva um programa que pergunte o salário de um funcionário e calcule seu valor do

seu aumento.

Para salários superiores a R$1250,00, calcule um aumento de 10%.

Para os inferiores ou iguais, o aumento é de 15%.

'''



s = float(input('Por favor digite o valor do seu salário para saber qual o seu aumento\n'

                'R$'))

if s > 1250:

    a = s * 1.1

    print('Seu novo salário será R${:.2f}'.format(a))

else:

    a = s * 1.15

    print('Seu novo salário será R${:.2f}'.format(a))
