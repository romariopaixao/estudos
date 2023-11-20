import pymysql.cursors

try:
    conexao = pymysql.connect(host='localhost', user='root', password='', database='escola', cursorclass=pymysql.cursors.DictCursor)
    print('Conexão estabelecida')
except Exception as error:
    print(f'Erro ao estabelece conexão! Erro: {error}')

cursor = conexao.cursor()

def select():
    try:
        sql = "SELECT * FROM alunos"
        cursor.execute(sql)
        alunos = cursor.fetchall()
        for aluno in alunos:
            print(aluno)
    except Exception as erro:
        print(f'Erro ao buscar os alunos! Erro: {erro}')

def insert(nome: str, idade: int, curso: str, nota: float):
    try:
        sql = "INSERT INTO alunos (nome, idade, curso, nota) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, idade, curso, nota))
        conexao.commit()
        print('ALuno cadastrado com sucesso!')
    except Exception as erro:
        print(f'Erro ao cadastrar! Erro: {erro}')

def update(nome: str, idade: int, curso: str, nota: float, id: int):
    try:
        if verificaAlunoExist(id):
            sql = "UPDATE alunos SET nome = %s, idade = %s, curso = %s, nota = %s WHERE id = %s"
            cursor.execute(sql, (nome, idade, curso, nota, id))
            conexao.commit()
            print("Atualizado com sucesso !")
        else:
            print('Matrícula não encontrada.')
    except Exception as erro:
        print(f"Erro ao atualizar os dados! Erro: {erro}")


def delete(id: int):
    try:
        if verificaAlunoExist(id):
            sql = "DELETE FROM alunos WHERE id = %s"
            cursor.execute(sql, (id))
            conexao.commit()
            print("Aluno deletado com sucesso!")
        else:
            print("Matricula não cadastrada.")
    except Exception as erro:
        print(f"Erro ao deletar os dados! Erro: {erro}")

def verificaAlunoExist(id: int):
    sql = "SELECT * FROM alunos WHERE id = %s"
    cursor.execute(sql, (id))
    alunos = cursor.fetchall()
    if len(alunos) == 1:
        return True
    else:
        return False


delete(3)
select()
