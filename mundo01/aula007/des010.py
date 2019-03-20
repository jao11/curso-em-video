# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dolares ela pode comprar.
# considere: US$1,00=R$3,27
print('Por favor nos diga quanto você tem na carteira para que nós possamos converter o\n'
      ' seu dinheiro de reais para dolares:')
n = float(input('Digite aqui: R$'))
d = n / 3.27
print('Em dolares seu dinheiro tem o valor de US${:.2f}'.format(d))
