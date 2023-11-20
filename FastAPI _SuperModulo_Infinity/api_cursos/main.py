from fastapi import FastAPI, HTTPException, status, Response
from cursos import cursos
from models import Curso
app = FastAPI()

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):
    try:
        cursos[curso_id]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Curso não encontrado.'
        )
    else:
     return cursos[curso_id]
    
@app.post("/cursos")
async def post_curso(curso: Curso):
    try:
        cursos[curso.id]
    except KeyError:
        cursos[curso.id] = curso
        return cursos
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=f"Já existe com este ID: {curso.id}"
        )
    
@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id: {curso_id}'
        )


@app.put("/cursos/{curso_id}")
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos.keys():
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe um curso com o id {curso_id}'
        )



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)

