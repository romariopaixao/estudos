from fastapi import FastAPI, status
from typing import Dict
from criar_banco import *
from models import *

app = FastAPI(
    title='Restaurante Infinity',
    version='2.0',
    description='API para consulta e inserção de dados num restaurante',
    contact={
        'name':'Romario',
        'url':'https://www.linkedin.com/in/romariopaixao',
        'email':'romagalera@gmail.com'
    }
)
'''
Listar Cardário: Permita que os cleintes obtenham uma lista de itens do cardápio, incluindo detalhes como nome, descrição, preço e categoria.
GET /menu
'''

@app.get("/menu",
         description='Retorna todos os menus cadastrado no banco de dados',
         summary='retorna todos os menus',
         response_model=Dict[str, Menu],
         response_description='Menus encontrados'
         )
async def get_menu():
    return retornar_itens()

@app.get("/menu/{item}")
async def get_especific_menu(item):
    return retornar_item_especifico(item)





@app.post('/pedidos', status_code= status.HTTP_201_CREATED)
async def post_pedido(pedido: Pedido):
    inserir_pedido(
        pedido.nu_pedido,
        pedido.itens,
        pedido.status,
        pedido.total
    )
    return 'Pedido cadastrado com sucesso.'

@app.post("/menu", status_code = status.HTTP_201_CREATED)
async def post_menu(menu: Menu):
    inserir_menu(menu.item, menu.valor, menu.id_categoria, menu.descricao)
    return "cadastrado com sucesso"


if __name__ == '__main__':
    import uvicorn
    criar_banco()

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)