from fastapi import FastAPI,Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = FastAPI()
security = HTTPBasic()

def criar_banco():
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (user text, senha text)')

def criar_banco2():
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS estoque (prato text, qtd_prato integer)')

def retornar_usuario(user):
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    return cursor.execute(f'SELECT * from usuarios where user = "{user}"').fetchall()

def retornar_prato(prato):
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    return cursor.execute(f'SELECT * from estoque where prato = "{prato}"').fetchall()


@app.post("/cadastros")
def cadastrar(user: str, senha: str):
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    cursor.execute(f'''
        INSERT INTO usuarios VALUES('{user}','{generate_password_hash(senha)}')
    ''') 
    con.commit()
    return 'USUÁRIO CADASTRADO COM SUCESSO.'


@app.post("/estoque")
def cadastrar_prato(name_prato: str, qtd_prato: int):
    con = sqlite3.connect('restaurante.db')
    cursor = con.cursor()
    cursor.execute(f'''
                   INSERT INTO estoque VALUES('{name_prato}', '{qtd_prato}')
                   ''')
    con.commit()
    return "Prato adicionado com sucesso!"
    

@app.get("/receitas")
def recuperar_receitas(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    user_digitado = credentials.username
    user_banco = retornar_usuario(user_digitado)[0][0]
    senha_digitada = credentials.password
    senha_banco = retornar_usuario(user_digitado)[0][1]
    if check_password_hash(senha_banco, senha_digitada) == True:
        return 'https://www.tudogostoso.com.br/receita/23-bolo-de-cenoura.html'
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Credenciais Inválidas'
        )



if __name__ == "__main__":
    import uvicorn
    criar_banco()
    criar_banco2()
    uvicorn.run("app:app",host="0.0.0.0", port = 8000, reload=True)