from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from fastapi import Depends, HTTPException, status, FastAPI
from banco import usuarios
import secrets

security = HTTPBasic()
app = FastAPI()



@app.get("/")
def retornar_usuario(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    username_recebido_bytes = credentials.username.encode("utf8")
    username_correto_bytes = usuarios['user']
    comparacao_user = secrets.compare_digest(username_recebido_bytes, username_correto_bytes)

    senha_recebida_bytes = credentials.password.encode("utf8")
    senha_correta_bytes = usuarios['senha']
    comparao_senha = secrets.compare_digest(senha_recebida_bytes, senha_correta_bytes)

    if comparao_senha and comparacao_user:
        return 'AUTENTICAÇÃO REALIZADA COM SUCESSO.'
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "Credenciais Inválidas."
        )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)