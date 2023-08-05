'''1. Escreva um programa que lê o nome e o telefone de n contatos que será adicionado em uma agenda telefonica (dicionario)
1. a. O nome digitado será o nome da chave do dicionário, e o telefone será o valor
1. b. Encerre o programa quando o usuário digitar o nome "sair"
1. c. Imprima a agenda telefonica ao final

2. Após isso solicite o usuário um nome e busque este contato na lista, e exiba o telefone dele se ele existir.


João
85985525
{"João": "85985525"}
'''
nome = ''
numero = ''
listaTelefonica = {

        }

teste = ''
while True:
    teste = str(input('Deseja continuar: digite SIM ou NAO'))
    if teste == 'sim':
        nome = str(input('nome: '))
        # numero = str(input('numero: '))
        listaTelefonica[nome] = input('digite o numero')
    else:
        break

print(listaTelefonica)

# https://www.invertexto.com/619aula07