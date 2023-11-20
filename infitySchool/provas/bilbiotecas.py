import random
'''
[PY-A06]Considere o seguinte trecho de código em Python:

import random



lista = [1, 2, 3, 4, 5]

x = random.choice(lista)
'''

#a) Explique o que o código faz.
#A variavel x recebe um valor aleátorio dos numeros da lista
#b) Escreva um trecho de código que use a função random para gerar um número inteiro aleatório entre 10 e 20 (inclusive).
lista_numeros = []
for numero in range(10,21):
    lista_numeros.append(numero)
print(random.choice(lista_numeros))

#c) Escreva um trecho de código que use a função random para gerar uma lista com 5 elementos inteiros aleatórios entre 1 e 100 (inclusive).
lista_2 = []
lista_3 = []
for numero in range(1,101):
    lista_2.append(numero)

for i in range(5):
    lista_3.append(random.choice(lista_2))

print(lista_2)
print(lista_3)


