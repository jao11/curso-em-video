'''

Desenvolva um programa que pergunte a distância de uma viagem em km.

Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e

R$0,45 para viagens mais longas.

'''



d = float(input('Qual a distância da sua viagem em quilometros:'))

if d <= 200:

    p = d * 0.5

    print('Sua passagem vale R${:.2f}'.format(p))

else:

    p = d * 0.45

    print('Sua passagem valeR${:.2f}'.format(p))
