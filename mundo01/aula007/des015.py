# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60.00 por dia e R$0.15 por km rodado.
print('Olá, para saber quanto você irá pagar por favor digite abaixo.')
print('Quantos dias que você ficou com o carro?')
d = float(input('Digite aqui:'))
print('Quantos km você rodou com o carro?')
m = float(input('Digite aqui:'))
t = d * 60.00 + m * 0.15
print('Tendo rodado {} dias e {}km com o carro você nos deve R${:.2f}'.format(d, m, t))
