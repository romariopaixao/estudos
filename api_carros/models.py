from pydantic import BaseModel

class Carro(BaseModel):
    placa: str
    marca: str
    modelo: str
    ano: int
    status: str
    valor_compra: float

class Despesa(BaseModel):
    id_veiculo: int
    titulo: str
    valor_gasto: float
    descricao: str

class Venda(BaseModel):
    id_veiculo: int
    valor_vendido: float
    nome_comprador: str