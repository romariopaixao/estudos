import sqlite3

def conecta_banco(endereco):
    conn = sqlite3.connect(endereco)
    return conn