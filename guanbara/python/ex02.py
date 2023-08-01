'''nome = int(input("Digite seu nome:"))
print(f'Seja bem vindo {nome}!')
print(type(nome))'''

'''n1 = int(input("digite o primeiro numero:"))
n2 = int(input("digite o segundo numero:"))
soma = n1 + n2

print(f'A soma de {n1} + {n2} é {soma}')
print(n1.isnumber())
 sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado'''

km = float(input('Quantos km seu carro pecorreu? '))
dias = int(input('Quantos dia voce ficou com o carro? '))
total = dias * 60 + km / 0.15
print(f'O total a pagar é {total}')