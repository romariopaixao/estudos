# carrinho = ['luva', 'pastel', 'alface', 'framboesa']
# print(carrinho)
# print(max(carrinho))
# print(min(carrinho))

'''1. Considere a seguinte lista de numeros = [2, 5, 7, 9, 11, 12, 16, 18], utilize o laço for para
percorre-la sempre que o item for par imprima "este número é par" se o número for ímpar imprima "este número é ímpar"'''

# numeros = [2, 5, 7, 9, 11, 12, 16, 18]
# for i in numeros:
#     if i % 2 == 0:
#         print(f'{i} é um numero par')
#     else:
#         print(f'{i} é um numero impar')

'''2. Considere a mesma lista do exercicio anterior e informe a quantidade de pares e ímpares da lista'''

# par = 0
# impar = 0
# for i in numeros:
#     if i % 2 == 0:
#         par += 1
#     else:
#         impar += 1
# print(f'A lista tem {par} numeros par e {impar} numeros impares')

# 3. Considere a seguinte lista = [15, 7, 9, 14, 30, 99, 5, 8, 2, 12]e escreva um algoritmo para ordenar a lista em ordem crescente.
# lista = [15, 7, 9, 14, 30, 99, 5, 8, 2, 12]
# n = len(lista)
# #Algoritmo Selection Sort
# # Percorrendo os indices da lista
# for i in range(n):
#     # definir o indice atual
#     min_index = i
#     # procurando algum elemento com valor menor
#     # para armazenar seu indice
#     for j in range(i+1, n):
#         if lista[min_index] > lista[j]:
#             lista[j], lista[min_index] = lista[min_index], lista[j]
#
#     lista[i], lista[min_index] = lista[min_index], lista[i]
# print(lista)

tupla = (10, 5, 8, 12, 7,12)
