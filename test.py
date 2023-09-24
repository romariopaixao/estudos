""" def encontrar_elementos_comuns_e_soma(lista1, lista2):
    elementos_comuns = []
    soma = 0

    for elemento in lista1:
        if elemento in lista2:
            elementos_comuns.append(elemento)
            soma += elemento

    return (elementos_comuns, soma)

# Solicitar ao usuário as duas listas
lista1_str = input("Digite a primeira lista de números separados por vírgula: ")
lista2_str = input("Digite a segunda lista de números separados por vírgula: ")

# Converter as strings de entrada em listas de inteiros
lista1 = [int(x) for x in lista1_str.split(',')]
lista2 = [int(x) for x in lista2_str.split(',')]

# Chamar a função e imprimir o resultado
resultado = encontrar_elementos_comuns_e_soma(lista1, lista2)
print("Elementos em comum:", resultado[0])
print("Soma dos elementos em comum:", resultado[1]) """
# pessoas = {
#     "João": 23,
#     "Maria": 28,
#     "Pedro": 35,
#     "Lucas": 19
# }
#
# idade_joao = pessoas["João"]
# print(idade_joao)
#
# pessoas["Ana"] = 31
# print(pessoas)
#
# def maior_idade(dic):
#     maior = max(dic.values())
#     for nome, idade in dic.items():
#         if idade == maior:
#             return nome
#
# pessoas = {
#     "João": 23,
#     "Maria": 28,
#     "Pedro": 35,
#     "Lucas": 19
# }

# nome_mais_velho = maior_idade(pessoas)
# print("A pessoa mais velha é:", nome_mais_velho)

def maior_numero(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Exemplo de uso:
numero1 = 10
numero2 = 5
resultado = maior_numero(numero1, numero2)
print("O maior número é:", resultado)

def maior_numero(num1, num2):
    return max(num1, num2)

# Exemplo de uso:
numero1 = 10
numero2 = 5
resultado = maior_numero(numero1, numero2)
print("O maior número é:", resultado)

