from fastapi import FastAPI, status
from conecta_banco import *
from models import *

app = FastAPI(
    title = 'CARCRUD',
    version = '1.0',
    description= 'API do app CARCRUD, a qual permite cadastrar um veículo, uma despesa e uma venda. Além de receber o resumo do veículo.', 
    contact={
        "name":"Romario ",
        'url': 'https://github.com/romariopaixao',
        'email':  'romagale@gmail.com'
    }
)

@app.post('/cadastrar_veiculo',
          description='Cadastra um novo veículo no banco de dados.',
          summary = 'Cadastra um novo veículo.',
          response_description='Veículo Cadastrado com  sucesso.',
          status_code=status.HTTP_201_CREATED
          )
def cadastrar_veiculo(Carro: Carro):
    return salvar_carro(Carro.placa, Carro.marca, Carro.ano, Carro.modelo, Carro.status, Carro.valor_compra)

@app.get("/visualizar_veiculos",
         description='Mostra todos os veículos cadastrados no banco de dados ou um veículo em específico.',
         summary='Mostra todos os veículos.',
         response_description='Veículos',
         status_code= status.HTTP_200_OK
         )
def visualizar_veiculos(placa: str = None):
    if placa != None:
        return consultar_carro_especifico(placa)
    else:
        return consultar_carros()
    
@app.post('/cadastrar_despesa',
          description='Cadastra uma nova despesa no banco de dados.',
          summary='Cadastra uma nova despesa.',
          response_description='Nova Despesa',
          status_code = status.HTTP_201_CREATED
          )
def cadastrar_despesa(despesa: Despesa):
    salvar_despesa(despesa.id_veiculo, despesa.titulo, despesa.valor_gasto, despesa.descricao)
    return 'DESPESA CADASTRADA COM SUCESSO!'

@app.get(
    '/consultar_despesas_veiculo',
    description='Consulta depesas de um veículo em específico',
    summary='Consulta uma despesa.'
    ,response_description = 'consultar despesa',
    status_code=status.HTTP_200_OK
)
def  consultar_despesas_veiculo(id_veiculo:int):
    return consultar_despesa_veiculo(id_veiculo)

@app.post('/cadastrar_venda',
         description="Cadastra uma nova venda no banco ded dados.",
         summary="Cadastra uma nova venda.",
         response_description="Nova venda",
         status_code= status.HTTP_201_CREATED
         )
def cadastrar_venda(venda: Venda):
    salvar_venda(venda.id_veiculo, venda.valor_vendido, venda.nome_comprador)
    return 'VENDA CADASTRADA COM SUCESSO!'

@app.get("/consultar_venda",
        description='Consulta venda de um veículo em específico',
        summary='Consulta uma venda.',
        response_description = 'consultar venda',
        status_code=status.HTTP_200_OK
         )
def consultar_venda_veiculo(id_veiculo:int):
    return consultar_venda(id_veiculo)
    
@app.get("/resumo_veiculo")
def gerar_resumo_veiculo(id_veiculo:int):
    valor_comprado, total_despesas, total_vendido = gerar_resumo_carro(id_veiculo)
    resposta = {"valor_comprado": valor_comprado,
                "total_despesas": total_despesas,
                "total_vendido": total_vendido,
                "resumo": total_vendido - (total_despesas + valor_comprado)}
    return resposta
if __name__ == "__main__":
    import uvicorn
    criar_tabelas()
    uvicorn.run("app:app", host="0.0.0.0", port = 8000, reload=True)