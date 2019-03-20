# Crie um algoritimo que mostre seu dobro, triplo e raiz quadrada.
n = float(input('Por favor, você poderia digitar um número?\n'))
d = n * 2
t = n * 3
rq = n ** (1/2)
print('Você sabia que o dobro, o triplo e a raiz quadrada desse número são '
      'respectivamente {}, {} e {:.3f}'.format(d, t, rq))
