# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de
# desconto.
print('Para saber de qual será o novo preço, por favor digite o preço original do produto.')
p = float(input('R$'))
d = p * 95 / 100
print('O preço com 5% de desconto é R${:.2f}!'.format(d))
