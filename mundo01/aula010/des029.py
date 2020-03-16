'''

Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.

A multa vai custar R$ 7,00 por cada km/h acima do limite.

'''



v = float(input('Qual foi a sua velocidade ao passar pelo radar?'

                '\n Diga aqui:'))

if v > 80:

    m = (v - 80) * 7

    print('Você foi multado e o valor da sua multa é de R${:.2f}.'.format(m))

else:

    print('Você não foi multado.')
