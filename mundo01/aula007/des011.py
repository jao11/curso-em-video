# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua
# área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta
# pinta uma área de 2m².
print('Para saber quanto de tinta você precisará comprar para pintar sua parede, por \n '
      'favor digite o altura e a largura dela:')
h = float(input('altura:'))
l = float(input('largura:'))
a = (h * l)/2
print('Você deve comprar {:.3f} litros de tinta!'.format(a))

