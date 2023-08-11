'''Escreva um loop for que imprima os números pares de 1 a 10.'''
# for i in range(11):
#     print(i)
'''Crie um loop for que itera sobre uma lista de nomes e imprime cada nome em maiúsculas.'''
# nomes = ['romario', 'isabel', 'ruan', 'tayna', 'ninha']
# for nome in nomes:
#     print(nome.upper())

'''Utilizando um loop for, calcule a soma dos primeiros 100 números inteiros positivos.'''
# s = 0
# for i in range(101):
#     s += i
# print(s)

'''Como você imprimiria a tabuada do número 7 usando um loop for?'''
# for i in range(11):
#     print(f'{i} x 7 = ', i*7)

'''Escreva um loop for que itere sobre uma string e conte quantas vezes a letra "a" 
aparece nela.'''
# nome = 'Romarioa aa aa'
# n = 0
# for i in nome:
#     if i == 'a':
#        n += 1
# # print(nome.count('a'))
# print(n)


'''Implemente um loop while que conte de 5 até 15 e imprima cada número.'''
# inicio = 4
# final = 15
# while inicio < final:
#     inicio += 1
#     print(inicio)

'''Utilize um loop while para encontrar o menor múltiplo comum 
(MMC) de dois números inteiros positivos.'''

'''Escreva um loop while que gere números Fibonacci até que o valor ultrapasse 1000.'''
# n1 = 0
# n2 = 1
# soma = n1 + n2
# while n2 <= 1000:
#     n1 = n2
#     n2 = soma
#     soma = n1 + n2
#     print(soma, end=' ')

# a, b = 0, 1
#explicação do gpt
# while a <= 1000:
#     print(a, end=' ')
#     a, b = b, a + b

'''Crie um programa que peça ao usuário para adivinhar um número entre 1 e 100. 
Use um loop while para fornecer dicas até que o usuário adivinhe corretamente.'''
# numero = 32
# palpite = 0
# cont = False
# while cont == False:
#     if palpite > numero:
#         print('Você chutou acima do numero correto.')
#     elif palpite < numero:
#         print('Você chutou abaixo do numero correto.')
#     elif palpite == numero:
#         print(f'Parabéns ! voce acertou o numero escolhido {numero}')
#         cont = True
#     palpite = int(input('Digite seu palpite: '))

'''Implemente um loop while que leia números do usuário até que ele insira um número negativo. 
Em seguida, calcule e imprima a média dos números inseridos.'''
count = 0
n1 = 0
while True:
    numero = int(input('Digite um valor'))
    if numero < 0:
        break
    count += 1
    n1 += numero
    print(n1)

print('Media final =', n1/count)

