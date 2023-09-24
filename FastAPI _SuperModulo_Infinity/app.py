from fastapi import FastAPI
from frase import frases

app = FastAPI()

@app.get("/frases")
async def get_frases():
    return frases

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)