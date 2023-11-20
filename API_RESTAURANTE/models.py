from typing import Optional
from pydantic import BaseModel

class Menu(BaseModel):
    item: str
    valor: float
    id_categoria: int
    descricao: str

'''numero do pedido'''
class Pedido(BaseModel):
    nu_pedido: int
    itens: list
    status: str
    total: float