# Crie um programa que leia a temperatura em celsius e a converta para fahrenheit.
print('Nós gostariamos que você nos informasse a sua temperatura em ºC.')
C = float(input('Por favor, digite aqui:'))
F = ((C*9)/5)+32
print('Sua temperatura em fahrenheit é {:.2f}ºF'.format(F))