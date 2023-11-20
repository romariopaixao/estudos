import jwt
from fastapi import FastAPI, HTTPException, Header,status
from conecta_banco import conecta_banco
from criar_tabelas import criar_tabelas



app = FastAPI()

def inserir_usuarios(user, senha):
    try:
        conexao = conecta_banco('usuarios.db')
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO usuarios VALUES('{user}','{senha}')")
        conexao.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f'Erro ao inserir usuário no banco: {e}'
            )

def recuperar_usuarios(user,senha):
    cursor = conecta_banco('usuarios.db').cursor()
    resposta = cursor.execute(f"SELECT user, senha FROM usuarios WHERE user = '{user}' and senha = '{senha}'").fetchall()
    return resposta[0]

def gerar_token(user,senha):
    usuario, psw = recuperar_usuarios(user,senha)
    dados = {
        "user": usuario,
        "senha": psw
    }
    token = jwt.encode(dados, "secret", algorithm="HS256")
    return token

def verificar_token(token):
    try:
        dados = jwt.decode(token,"secret",algorithms=['HS256'])
        return dados
    except jwt.exceptions.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='TOKEN INVÁLIDO.')

@app.post("/cadastrar")
def cadastro(usr:str, senha:str):
    inserir_usuarios(usr, senha)
    return gerar_token(usr,senha)

@app.get("/")
def principal(token: str = Header(default=None)):
    return verificar_token(token)

if __name__ == "__main__":
    import uvicorn
    criar_tabelas()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)