from conecta_banco import conecta_banco


def criar_tabelas():
    cursor = conecta_banco('usuarios.db').cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (user text, senha text);            
''')
    conecta_banco('usuarios.db').commit()