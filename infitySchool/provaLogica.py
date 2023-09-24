'''[PY-A01]Faça um programa em Python que, utilizando estruturas de repetição,
calcule a média de idade dos alunos de uma turma. O programa deve pedir ao usuário a
quantidade de alunos na turma e, em seguida, solicitar a idade de cada um. O programa
deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para realizar
a soma das idades. Ao final, o programa deve exibir a média de idade da turma.'''

# qnt_alunos = int(input('Digite a quantidade de alunos na turma: '))
# idade_alunos = 0
#
# for i in range(qnt_alunos):
#     idade_alunos += int(input(f"Digite a idade do aluno {i+1}: "))
#
# media = idade_alunos / qnt_alunos
# print(f'A média de idade da turma é {media}')


#
# count = 0
# num_par = []
# while count <= 4:
#     n = int(input('Digite um numero entre 0 e 10: '))
#     if n % 2 == 0:
#         num_par.append(n)
#     count += 1
#
# print(num_par)

# # Solicitar ao usuário que digite três números
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))
#
# # Inicializar as variáveis para armazenar o maior e o menor número
# maior = num1
# menor = num1
#
# # Verificar e atualizar o maior número
# if num2 > maior:
#     maior = num2
# if num3 > maior:
#     maior = num3
#
# # Verificar e atualizar o menor número
# if num2 < menor:
#     menor = num2
# if num3 < menor:
#     menor = num3
#
# # Verificar se existem números iguais
# # iguais = []
# #
# # if num1 == num2:
# #     iguais.append(num1)
# #     iguais.append(num2)
# #
# # if num1 == num3:
# #     iguais.append(num1)
# #     iguais.append(num3)
# #
# # if num2 == num3:
# #     iguais.append(num2)
# #     iguais.append(num3)
# #
# # # Imprimir os resultados
# # print("O maior número é:", maior)
# # print("O menor número é:", menor)
# #
# # if len(iguais) > 0:
# #     print("Existem números iguais:", iguais)
# # else:
# #     print("Não existem números iguais.")
help(max)