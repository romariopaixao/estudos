# importando sqlite
import sqlite3 as lite

# criando
con = lite.connect('dados.db')

# dados = ['vaso', 'sala de estar', 'vaso que comprei no mercado ao lado', 'Marca x', '27/08/2022', '100', 'xxxx', 'c:imagem' ]
# # inserir dados
# with con:
#     cur = con.cursor()
#     query = 'INSERT INTO inventorio(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
#     cur.execute(query, dados)

ver_dados = []
# Ver dados
with con:
    cur = con.cursor()
    query = 'SELECT * FROM inventorio'
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        ver_dados.append(row)

print(ver_dados)
