'''

condicionais

'''



# if carro.esquerda():     se...:

#   bloco True

# else:                    senão...:

#   bloco false

'''

tempo= int(input('quantos anos tem seu carro?'))

if tempo <= 3:

    print('carro novo')

else:

    print('carro velho')

# print('carro novo' if tempo<=3 else 'carro velho') essa é uma forma simplificada

print('--FIM--')

'''

'''

nome = str(input('Qual o seu nome'))

if nome == 'João':

    print('Que nome lindo vc tem!!')

else:

    print('Seu nome é normal!')

print('Bom dia, {}.'.format(nome))

'''



n1 = float(input('Por favor, digite a nota de P1:'))

n2 = float(input('Por favor, digite a nota da P2:'))

m = (n1 + n2) / 2

print('Sua média é {:.2f}'.format(m))

if m >= 7:

    print('Portanto você passou.')

elif 7 > m >= 4:

    print('Você vai para a prova final.')

else:

    print('Você reprovou')

