# desenvolva um programa que pergunte a distancia dce uma viagem em km. calcule o
# preço da passagem, cobrando 0,50 por km para viagens ate 200km e 0,45 para viagens mais longas

# distanciaTotal = float(input('Digite a kilometragem da sua viagem: '))
# preco = distanciaTotal * 0.5 + distanciaTotal
# precoPromo = distanciaTotal * 0.45 + distanciaTotal
#
# if distanciaTotal <= 200:
#     print(f'O valor por km da sua viagem foi 0.50. Total = {preco}')
# else:
#     print(f'O valor promocional por km da sua viagem foi 0.45. Total = {precoPromo}')


# verificador: 0
# while True:
#     n1 = int(input('Digite o primeiro numero: '))
#     n2 = int(input('Digite o segundo numero: '))
#     n3 = int(input('Digite o terceiro numero: '))
#     if n1 == n2 == n3:
#         print('Os numero são iguais')
#     elif n1 > n2 and n1 > n3 and n2 >= n3:
#         if n2 == n3:
#             print(f'{n1} é o maior numero e {n2} e {n3} são iguais, ambos sendo o menor numero')
#         print(f'O numero {n1} maior  e {n3} é o menor')
#     elif n1 > n2 and n1 > n3 and n3 >= n2:
#         print(f'O numero {n1} maior  e {n2} é o menor')
#     elif n2 > n1 and n2 > n3 and n1 >= n3:
#         if n1 == n3:
#             print(f'{n2} é o maior numero e {n1} e {n3} são iguais, ambos sendo o menor numero')
#         print(f'O numero {n2} maior  e {n3} é o menor')
#     elif n2 > n1 and n2 > n3 and n3 >= n1:
#         print(f'O numero {n2} maior  e {n1} é o menor')
#     elif n3 > n1 and n3 > n2 and n1 >= n2:
#         if n1 == n2:
#             print(f'{n3} é o maior numero e {n1} e {n2} são iguais, ambos sendo o menor numero')
#         print(f'O numero {n3} maior  e {n2} é o menor')
#     elif n3 > n1 and n3 > n2 and n2 >= n1:
#         print(f'O numero {n3} maior  e {n1} é o menor')
#
#     verificador = int(input('''Deseja testar de novo?
#     Digite 1 para Sim
#     Digite 2 para Não'''))
#     if verificador == 2:

# Se for acima de 1250 recebe 10% se for abaixo recebe 15%

salario = float(input('Digite seu salário: '))

if salario > 1250:
    salario = salario * 10 / 100 + salario
    print(f'Voce recebe acima de 1250, teve 10% de aumento e seu novo salario é = {salario}')
else:
    salario = salario * 15 / 100 + salario
    print(f'Voce recebe abaixo de 1250, teve 15% de aumento e seu novo salario é = {salario}')