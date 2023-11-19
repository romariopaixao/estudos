print('Ola mundo')

'''
[PY-A07]Você foi contratado para desenvolver um programa que calcule a média de notas dos alunos de uma turma. 
Para isso, você deverá criar uma lista com as notas de cada aluno e, em seguida, implementar uma função que calcule a 
média aritmética das notas. Além disso, você deverá utilizar um loop while para pedir ao usuário que insira as notas dos 
alunos até que ele decida parar. Por fim, você deverá utilizar um loop for para imprimir a média de cada aluno.

Observações:

a) Escreva o código para a função que calcule a média aritmética das notas.

b) Escreva o código para o loop while que pede ao usuário que insira as notas dos alunos.

c) Escreva o código para o loop for que imprime a média de cada aluno.

'''
# notas = []
# continuar = True
# while continuar:
#     nome_aluno = input(str('Digite o nome do aluno? '))
#     if nome_aluno != 'sair':
#         notas.append(nome_aluno)
#     else:
#         continuar = False
#
# print(notas)
# def media(list)

def calcular_media(notas):
    if not notas:
        return None  # Retorna None se a lista de notas estiver vazia

    soma = sum(notas)
    media = soma / len(notas)
    return media

# Lista para armazenar as notas de cada aluno
notas_alunos = []

# Loop while para receber as notas dos alunos
continuar = True

while continuar:
    notas = []  # Lista para armazenar as notas do aluno atual
    try:
        # Loop para receber as notas do aluno atual
        while True:
            nota = float(input("Digite a nota do aluno (ou digite um valor não numérico para encerrar): "))
            notas.append(nota)
    except ValueError:
        continuar = False  # Encerra a entrada ao digitar um valor não numérico
    if notas:  # Adiciona as notas do aluno atual à lista geral apenas se houver notas
        notas_alunos.append(notas)

# Loop for para imprimir a média de cada aluno
for indice, notas in enumerate(notas_alunos, start=1):
    media_aluno = calcular_media(notas)
    if media_aluno is not None:
        print(f"Média do Aluno {indice}: {media_aluno:.2f}")
    else:
        print(f"O Aluno {indice} não possui notas.")


