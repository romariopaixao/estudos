# lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
lanche = (7, 3, 2 ,9)

'''Nessa versão do for estou passando o lanche com posição dos itens na tupla'''
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer: {lanche[cont]}')

'''Nessa versão do for estou passando uma variavel com os itens da tupla'''
# for comida in lanche:
#     print(f'Eu vou comer: {comida}')

'''Nessa versão do for usa enumerate que ele pode receber 2 variaveis'''
# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

''''Metodo sorted mostra o codigo em ordem alfabetica ou numerica'''
# print(sorted(lanche))

'''vai printar de tras para frente ate o valor tres de tras pra frente'''
# print(lanche[-3:])

'''vai printar do inicio da tupla ate o 1'''
# print(lanche[:2])

'''-------------------------------------------'''
a = (1, 2, 5, 3, 5,)
b = (1, 4, 9, 8, 4, 6)
c = a + b
print(c)
'''tamanho da tupla'''
print(len(c))
'''numero de vezes que aparece o item 5 na tupla'''
print(c.count(5))
"em que posição esta o item 5"
print(c.index(5))
"em que posição esta o item 5 iniciando a contagem da posição 3"
print(c.index(5, 3))
'''deletando a tupla, so pode ser excluida inteira'''
del(a)

'''fazer os desafios amanha quando acordar'''