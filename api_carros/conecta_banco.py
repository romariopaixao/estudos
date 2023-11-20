import sqlite3

conexao = sqlite3.connect('D:\Estudos\\api_carros\db\carcrud.db', check_same_thread=False)

def criar_tabelas():
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
            VEICULO(
                   id_veiculo INTEGER PRIMARY KEY NOT NULL,
                   placa TEXT UNIQUE NOT NULL,
                   marca TEXT NOT NULL,
                   modelo TEXT NOT NULL,
                   ano INTEGER NOT NULL,
                   valor_de_compra REAL NOT NULL,
                   status TEXT
            )

        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
                   VENDA (
                    id_veiculo INTEGER NOT NULL,
                   valor_vendido REAL NOT NULL,
                   nome_comprador TEXT NOT NULL,
                   FOREIGN KEY(id_veiculo) REFERENCES VEICULO (id_veiculo)
                   )

        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS
                   DESPESAS(
                   id_veiculo INTEGER NOT NULL,
                   titulo text NOT NULL,
                   valor_gasto REAL NOT NULL,
                   descricao TEXT NOT NULL,
                   FOREIGN KEY(id_veiculo) REFERENCES VEICULO (id_veiculo)
                   )

    ''')


    conexao.commit()
def salvar_carro(placa, marca, ano, modelo, status, valor_compra, con=conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute(f'''
            INSERT INTO VEICULO 
                    (placa, marca, ano, modelo, status, valor_de_compra)
            VALUES (
                    '{placa}','{marca}', '{ano}', '{modelo}', '{status}', '{valor_compra}'
            )

        ''')
    except sqlite3.IntegrityError:
        return 'CAMPO VAZIO'
    else:
        conexao.commit()
        return 'DADOS DESTE CARRO FORAM SALVOS COM SUCESSO.'
    
def consultar_carros(con=conexao):
    cursor = conexao.cursor()
    return cursor.execute(f'''SELECT * FROM VEICULO;''').fetchall()
    

def consultar_carro_especifico(placa, con=conexao):
    cursor = conexao.cursor()
    return cursor.execute(f'''
        SELECT * FROM VEICULO WHERE PLACA = '{placa}'
    ''').fetchall()

def salvar_despesa(id_veiculo, titulo, valor_gasto, descricao, con=conexao):
    cursor = conexao.cursor()
    cursor.execute(f'''INSERT INTO DESPESAS (id_veiculo, titulo, valor_gasto, descricao)
                        VALUES
                        ('{id_veiculo}','{titulo}','{valor_gasto}','{descricao}')
                   ''')
    con.commit()

def consultar_despesa_veiculo(id_veiculo, con=conexao):
    cursor=con.cursor()
    return cursor.execute(f'''
        SELECT id_veiculo, titulo, descricao, valor_gasto
            FROM DESPESAS WHERE id_veiculo = {id_veiculo};
    ''').fetchall()

def salvar_venda(id_veiculo, valor_vendido, nome_comprador, con=conexao):
    cursor = conexao.cursor()
    cursor.execute(f'''
                        INSERT INTO VENDA (id_veiculo, valor_vendido, nome_comprador) 
                        VALUES ('{id_veiculo}','{valor_vendido}','{nome_comprador}')
                    ''')
    con.commit()

def consultar_venda(id_veiculo, con=conexao):
    cursor=con.cursor()
    return cursor.execute(f'''
            SELECT id_veiculo, valor_vendido, nome_comprador FROM VENDA WHERE id_veiculo = {id_veiculo};
    ''').fetchall()

def gerar_resumo_carro(id_veiculo, con=conexao):
    cursor = conexao.cursor()
    total_despesas =  cursor.execute(f'''
        SELECT  sum(d.valor_gasto) from VEICULO v INNER JOIN DESPESAS D on v.id_veiculo = d.id_veiculo 
                   INNER JOIN VENDA ve ON ve.id_veiculo = v.id_veiculo
    ''').fetchall()[0][0]
    valor_comprado = cursor.execute(f'''
        select valor_de_compra FROM VEICULO where id_veiculo = {id_veiculo}
        ''').fetchall()[0][0]
    total_vendido = cursor.execute(f'''
        select valor_vendido from VENDA where id_veiculo = {id_veiculo}
        ''').fetchall()[0][0]
    resumo = total_vendido - valor_comprado - total_despesas
    return valor_comprado, total_despesas, total_vendido



        
