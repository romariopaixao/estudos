#CRUD
banco = [
    {'matricula': 1, 'nome':'Elisa', 'curso':'Python'},
    {'matricula': 2, 'nome': 'Mariana', 'curso':'Javascript'}
]

matricula_atual = 2

def cadastrarAluno(nome, curso):
    global matricula_atual
    matricula_atual += 1
    aluno = {
        'matricula':matricula_atual,
        'nome':nome,
        'curso':curso
    }
    banco.append(aluno)
    print('Aluno cadastrado com sucesso!')

def editarAluno(matricula):
    alunoExiste = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            aluno['nome'] = input('Digite o novo nome: ')
            aluno['curso'] = input('Digite o novo curso: ')
            alunoExiste = True
            print('Dados alterados com sucesso !')
    if alunoExiste == False:
        print('Aluno não encontrado')

def buscarAluno(matricula):
    alunoExiste = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            print('--- DADOS DO ALUNO ----')
            print(f'Matricula: {aluno["matricula"]}')
            print(f"Aluno: {aluno['nome']}")
            print(f"Curso: {aluno['curso']}")
            alunoExiste == True
    if not alunoExiste:
        print("Aluno não encontrado!")

def delAluno(matricula: int):
    alunoExiste = False
    for aluno in banco:
        if aluno['matricula'] == matricula:
            banco.remove(aluno)
            print('Aluno removido com sucesso! ')
            alunoExiste = True
    if not alunoExiste:
        print('Aluno não encontrado!')


while True:
    print("----- Bem vindo ao menu -----")
    opcao = int(input("1 - Cadastrar aluno \n"
                      "2 - Editar aluno \n"
                      "3 - Buscar aluno \n"
                      "4 - Deletar aluno \n"
                      "5 - Listar todos os alunos \n"
                      "6 - Sair \n"
                      "Selecione uma opção: "))

    if opcao == 1:
        nome = input('Digite o nome do aluno: ')
        curso = input('Digite o curso do aluno: ')
        cadastrarAluno(nome, curso)
    elif opcao == 2:
        matricula = int(input('Digite a matricula que deseja editar: '))
        editarAluno(matricula)
    elif opcao ==3 :
        matricula = int(input('Digite a matricula que deseja buscar: '))
        buscarAluno(matricula)
    elif opcao == 4:
        matricula = int(input('Digite a matricula do aluno que deseja excluir: '))
        delAluno(matricula)
    elif opcao == 5:
        print('--='*40)
        print(banco)
        print('--='*40)
    elif opcao == 6:
        break
    else:
        print('Código inválido')