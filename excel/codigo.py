#pandas -> bases de dados
#os -> arquivo do coputador
#pywin32 -> enviar email
import os
import pandas as pd

caminho = "bases"
arquivos = os.listdir(caminho)
print(arquivos)

tabela_consolidada = pd.DataFrame()

for nome_arquivo in arquivos:
    tabela_vendas = pd.read_csv(os.path.join(caminho, nome_arquivo))
    tabela_vendas["Data de Venda"] = pd.to_datetime("01/01/1900") - pd.to_timedelta(tabela_vendas["Data de Venda"], unit="d")
    print(tabela_vendas)
