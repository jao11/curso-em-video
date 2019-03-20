# Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.
print('Você vai ter um aumento de 15% no seu salário, para saber o novo valor,\n'
      'por favor digite o valor atual do seu salário.')
s = float(input('R$'))
a = s * 15 / 100 + s
print('O seu novo salário será R${:.2f}'.format(a))
