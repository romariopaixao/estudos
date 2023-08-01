'''import math

num = int(input("digite um valor "))
raiz = math.sqrt(num)

print(f'A raiz quardad de {num} é {(raiz):.2f}')
Exercicio 16
import math
num = float(input("digite um valor quebrado"))
arredondamento = num // 1
print(f'O numero digitado foi {num} e sua porção inteira é {arredondamento}')

from math import hypot
ca = float(input('digite cateto'))
co = float(input('digite coseno'))
hi = hypot(ca, co)
print(hi)'''

# import random
# n1 = str(input('nome 1 '))
# n2 = str(input('nome 2'))
# n3 = str(input('nome 3'))
# n4 = str(input('nome 4'))
# lista = [n1, n2, n3, n4]
# random.shuffle(lista)
# print(lista)
from time import sleep
continuar = 0
while True:
    if continuar == 2:
        break

    n1 = int(input('Digite o numero para a operação: '))
    print('-=-'*20)
    n2 = int(input('Digite outro numero para a operação: '))
    print('-=-'*20)
    adicao = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2
    resultado = 0

    operacao = int(input('''
    Digite o numero equivalente a sua operação:
    1- Soma
    2- Subtração
    3- Multiplicação
    4- Divisao:
    '''))

    # print('CARREGANDO...')
    # print(sleep(3))
    if operacao == 1:
        resultado = n1 + n2
    elif operacao == 2:
        resultado = n1 - n2
    elif operacao == 3:
        resultado = n1 * n2
    elif operacao == 4:
        resultado = n1 / n2

    print(f'O resultado foi : {resultado}')

    continuar = int(input(f'Deseja fazer outra operação: 1- Sim.  ||  2- Não. '))







