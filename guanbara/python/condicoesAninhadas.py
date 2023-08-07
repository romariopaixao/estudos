'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma cas.
O prgrama vai perguntar o valor da cas, o salario do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mental, sabendo que ela nao pode exceder 30% do salario ou entao
o emprestimo sera negado.'''
# casa = float(input("valor da casa: "))
# salario = float(input("valor do salario"))
# ano = int(input("quantos anos para pagar: "))
# parcela = casa / (ano * 12)
# corte = salario * 30 / 100
#
# print(f'O valor da parcela fica: {parcela}')
# if parcela > corte:
#     print(f'Emprestimo negado. As parecelas de {parcela} ultrapassam 30% do seu salario que é {corte}')

'''Escreva um programa que lai dois numero interios e compare-os', mostrando na tela uma mensagem:
-o primeiro valor é maior
-o segundo valor é maior
-nao existe valor maios os dois sao iguais'''
# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite outro valor: '))
# if n1 > n2:
#     print(f'O primeiro numero é maior.')
# elif n2 > n1:
#     print(f'O segundo valor é maior.')
# elif else:
#     print('Os valores são iguais.')

'''Leia o ano de nascimento, informe sua idade e diga:
- Se ele ainda vai se alistar
- Se é a hora de se alistar
- Se ja passou do tempo de alistamento.
-Quando tempo falta pra alistar
- Quando tempo passou do alistamento.'''

# ano = int(input('Digite o ano do seu nascimento: '))
# idade = 2023 - ano
# falta = 18 - idade
# passou = idade - 18
# print(idade)
# if idade < 18:
#     print(f'Voce ainda vai se alistar. Faltam {falta} anos')
# elif idade == 18:
#     print('Voce está na hroa de se alistar')
# elif idade > 18:
#     print(f'Voce ja passou {passou} anos do tempo de se alistar')

'''Leia duas notas e calcule a media e mostre:
- Media abaixo de 5 REPROVADO
- mEDIA ENTRE 5 E 6,9 RECUPERAÇÃO
- Media 7 ou superior APROVADO'''
# n1 = float(input('Digite sua primeira nota: '))
# n2 = float(input('Digite sua segunda note: '))
# media = (n1 + n2) / 2
# print(media)
#
# if media < 5.0:
#     print('REPROVADO')
# elif media >= 5.0 and media <= 6.9:
#     print('RECUPERAÇÃO')
# elif media >= 7:
#     print('APROVADO')

'''Leia o ano de nascimento e mostre a categoria:
= ate 9 anos MIRIM
- Ate 14 INFANTIL
- Ate 19 JUNIOR
- Ate 20 SENIOR
- Acima MASTER'''
# ano = int(input('Digite seu ano de nascimento'))
# idade = 2023 - ano
# print(idade)
# if idade <= 9:
#     print('MIRIM')
# elif idade <= 14 and idade > 9:
#     print('INFANTIL')
# elif idade <= 19 and idade > 14:
#     print('JUNIOR')
# elif idade == 20:
#     print('SENIOR')
# else:
#     print('MASTER')

'''Receba altura e peso e mostre de acordo com o IMC:
- Abaixo de 18.5 ABAIXO DO PESO
- Entre 18.5 e 25 PESO IDEAL
- 25 ate 30: SOBREPESO
- 30 ATE 40 OBESIDADE
- ACIMA DE 40 OBESIDADE MORBBIDA'''

'''Calcule o valro a ser pago por um produto considerando o seu preço normal 
e condição de pagamento:
- A vista DINHERO OU CHEQUE: 10% DE DESCONTO
- A vista no cartao: 5% de desconto:
- Em ate 2x no cartao: PREÇO NORMAL
- 3x ou mais no cartao: 20% de juros.'''

'''Crie um programa que faça o computador jgoar jokenpo com voce'''