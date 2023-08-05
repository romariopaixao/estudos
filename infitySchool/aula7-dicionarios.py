#dicionario
#estrutura chave:valor

#como criar um dicionário
fiado = {
    "marcos":155.90,
    "jose":90.0
}
eu = {
    'nome':None,
    'idade':None,
    'profissao':None,
    'salario':None,
    'IR':None,
}
# eu['nome'] = str(input('digite seu nome: ')).split()
# eu['idade'] = int(input('digite sua idade: '))
# eu['profissao'] = str(input('digite sua profissao: ')).split()
# # eu['salario'] = float(input('Digite seu salario: '))


'''2. Crie uma nova chave chamada "IR", que vai depender da seguinte condição
> Se o valor na chave salario for abaixo de 2000. A chave "IR" irá armazenar o valor "insento"
> Se o valor na chave salario for acima de 2000. A chave "IR" irá armazenar o valor "contribuinte"'''
eu['salario'] = float(input('Digite seu salario: '))
if eu['salario'] < 2000:
    eu['IR'] = 'insento'
else:
    eu['IR'] = 'contribuinte'

#como deletar uma propiedade em um dicionario
del eu['IR']
print(eu)

# for key in dados:
#     print(dados[key])


# Imprime todas as chaves do dicionário
print(dados.keys())

# Imprime todos os valores do dicionário
print(dados.values())
for valor in dados.values():
    print(valor)

# Imprime todos os itens do dicionário
print(dados.items())

# dados["salario"] = float(input('Digite o seu salário: '))
# if dados['salario'] < 2000:
#     dados["IR"] = "insento"
# else:
#     dados["IR"] = "contribuinte"
#
# print(dados)