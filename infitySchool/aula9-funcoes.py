#Tranferencia:


''''1. Escreva uma função que lê base e altura de um triangulo, calcule sua área e exiba na tela
area = base * altura / 2 '''
# def areaTriangulo():
#     base = int(input('Difite a base do seu triangulo: '))
#     altura = int(input('Digite a altura do seu triangulo: '))
#     area = base * altura / 2
#     print(f'A área do seu triangulo é {area}')
#
# areaTriangulo()
'''2. Escreva uma função que lê um número e informa se ele é par ou ímpar '''
# def parOuImpar():
#     n = int(input('Digite o seu numero para teste: '))
#     if n % 2 == 0:
#         print('Seu numero é par!')
#     else:
#         print('Seu numero é impar!')
# parOuImpar()

'''3. Escreva uma função que lê dois números e imprima o maior ou se eles são iguais'''
# def maiorNumero():
#     n1 = int(input('Digite um numero: '))
#     n2 = int(input('Digite outro numero:'))
#     if n1 > n2:
#         print(f'O numero {n1} é maior do que o {n2}')
#     elif n2 > n1:
#         print(f'O numero {n2} é maior do que o {n1}')
#     else:
#         print('Os numero são iguais')
#
# maiorNumero()

'''4. Escreva uma função que lê 10 números e imprima a quantidade de números pares digitados'''
# def numerosPares():
#     count = 0
#     for i in range(10):
#         n1 = int(input('Digite um numero: '))
#         if n1 % 2 == 0:
#             count += 1
#     print(f'A quantidade de numeros pares digitas foi {count}')
#
# numerosPares()

'''Cria uma função que leia n numero e ao final informe a quantidade de primos digitados
primo = divisivel por 1 e ele mesmo'''

# def primos():
#     while True:
#         numerosPrimos = []
#         n = int(input('Digite um numero: '))
#         if n % n == 0 and n % 1 == 0:
#             numerosPrimos.append(n)
#         elif n == -1:
#             break
#     print(numerosPrimos)
# primos()

'''1. Escreva uma função que recebe o raio de um circulo por parametro, e imprima a sua área
area = pi * raio ** 2'''
# def areaCirculo(raio):
#     area = 3.14 * raio ** 2
#     print(f'A área do ciruclo é : {area}')
#
# n = int(input('Digite o raio do seu circulo: '))
# areaCirculo(n)


'''2. Escreva uma função que recebe base maior, base menor e altura por parametro, calcule a area do trapezio e imprima o resultado
area = (base maior + base menor) * altura /2 '''

def areaTrapezio(bMaior, bMenor, altura):
    area = (bMaior + bMenor) * altura / 2
    print(f'A area do seu trapezio é {area}')

baseMaior = int(input('Digite o valor da sua base maior: '))
baseMenor = int(input('Digite o valor da sua base menor: '))
altura = int(input('Digite o valor da altura: '))
areaTrapezio(baseMaior, baseMenor, altura)