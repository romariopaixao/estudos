sumn = lambda n1, n2: n1 + n2
print(sumn(1,234))

'''
escreva uma função lambda para calcular a ara de um quadrado que recebe pro parametro um lado 
area = lado**2
'''
area = lambda lado: print(f'A area do quadrado é {lado ** 2}')
area(10)

'''
imc peso / altura ** 2
'''
# imc = lambda peso, altura: print(f'Seu imc é: {peso / altura ** 2}')
#
# imc(63,1.70)


def imc(peso: float, altura: float):
    return print(f'seu imc é: {peso / altura ** 2}')

imc(63.0,1.70)