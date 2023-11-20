import sqlite3

def criar_banco():
    banco = sqlite3.connect(
        "D:\\Estudos\\API_RESTAURANTE\\db\\restaurante.db"
        )

    cursor = banco.cursor()

    cursor.execute('''
        CREATE TABLE if not exists MENU(
                   item text,
                   valor float,
                   id_categoria integer,
                   descricao text)
        ''')
    cursor.execute('''
        CREATE TABLE if not exists PEDIDOS(
                nu_pedido integer,
                itens string,
                status string,
                total float );

    ''')

    banco.commit()

def inserir_menu(item: str,
                 valor: float,
                 id_categoria: int,
                 descricao: str):
    banco = sqlite3.connect(
        "D:\\Estudos\\API_RESTAURANTE\\db\\restaurante.db"
        )

    cursor = banco.cursor()

    cursor.execute(f'''
        INSERT INTO MENU values("{item}",{valor}, {id_categoria},"{descricao}")
        ''')
    banco.commit()


def retornar_itens():
    banco = sqlite3.connect(
        "D:\\Estudos\\API_RESTAURANTE\\db\\restaurante.db"
        )
    cursor = banco.cursor()
    
    resposta = {}
    consulta = cursor.execute('''
        SELECT * FROM MENU ''').fetchall()
    for tupla in consulta:
        resposta[tupla[0]]  = {"valor": tupla[1],
                               "id_categoria":tupla[2], 
                               "descricao": tupla[3]}

    return resposta

def retornar_item_especifico(item):
    banco = sqlite3.connect(
        "D:\\Estudos\\API_RESTAURANTE\\db\\restaurante.db"
        )
    
    cursor = banco.cursor()
    resposta = {}
    consulta = cursor.execute(f'''
        SELECT * FROM MENU WHERE item = '{item}'
''')
    for tupla in consulta:
        resposta[tupla[0]] = {"valor": tupla[1],
                               "id_categoria":tupla[2], 
                               "descricao": tupla[3]} 
    return resposta


def inserir_pedido(nu_pedido: int, itens: list, status: str, total: float):
    banco = sqlite3.connect(
        "D:\\Estudos\\API_RESTAURANTE\\db\\restaurante.db"
        )
    cursor = banco.cursor()

    cursor.execute(f'''INSERT INTO PEDIDOS values({nu_pedido},"{itens}","{status}",{total});
''')
    banco.commit()