from fastapi import FastAPI
from frase import frases
#instanciando classe fastapi
app = FastAPI()

#criando endpoint que retorna todas as frases do dicionario
@app.get("/frases")
async def get_frases():
    return frases

#passando argumentos
@app.get("/calculadora")
async def somar(a:int, b:int, c:int):
    return {"resultado": a+b+c}

#endpoint que retorna so uma frase expecifica
@app.get("/{id_frase}")
async def get_frase(id_frase):
    return frases[int(id_frase)]

#inificando servidor
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)