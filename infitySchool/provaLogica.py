'''[PY-A01]Faça um programa em Python que, utilizando estruturas de repetição,
calcule a média de idade dos alunos de uma turma. O programa deve pedir ao usuário a
quantidade de alunos na turma e, em seguida, solicitar a idade de cada um. O programa
deve utilizar um laço FOR para receber as idades dos alunos e um laço WHILE para realizar
a soma das idades. Ao final, o programa deve exibir a média de idade da turma.'''

qnt_alunos = int(input('Digite a quantidade de alunos na turma: '))
idade_alunos = 0

for i in range(qnt_alunos):
    idade_alunos += int(input(f"Digite a idade do aluno {i+1}: "))

media = idade_alunos / qnt_alunos
print(f'A média de idade da turma é {media}')


