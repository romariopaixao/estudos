from fastapi import FastAPI
from cursos import cursos

app = FastAPI()

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    return cursos[curso_id]

@app.get("/update_curso/{curso_id}")
async def update_curso(curso_id: int, horas: int):
    cursos[curso_id].update({"horas":horas})
    return cursos


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)

