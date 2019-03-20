# AULA 006
# n1=input('digite um número')
# n2=input('digite mais um número')
# s=n1+n2
# print('A soma vale',s)
# Infelizmente o algoritmo não vai funcionar se for escrito dessa forma.
# Para dar certo temos que escrever assim...
n1 = int(input('digite um número'))
n2 = int(input('digite mais um número'))
s = n1 + n2
print('A soma vale', s)
# print('A soma entre', n1,'e', n2, 'vale', s)
# format serve para ordenar as variaveis
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))

# Os tipos primitivos são:
# int(inteiro)(7), float(real)(7.0), bool(lógicos)(true or false), str(caracter)('olá')
print('A soma vale{}'.format(s))
# pint(type(n1)) para ver a classe do n1 coloca-se type
print(type(n1))
print(type(s))

n3 = bool(input('Digite um valor'))
print(n3)
# se tiver type bool e não tiver nada escrito no "digite um valor" vai aparecer como false
# se tiver algo vai aparecer true

n4 = input('Digite algo:')
print(n4.isnumeric())
# Esse comando serve para dizer se é falso ou verdadeiro, se é possivel converter em número
print(n4.isalpha())  # ve se converte em alfabetico4
# Os comandos is( alguma coisa servem para teste de true or false
print(n4.isprintable())

n5 = float(input('Digite um valor'))
print(n5)
