'''22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas;
- O nome com todas as letras minúsculas;
- Quantas letras ao todo(sem considerar espaços)
- How many lattes has the first name.
nome = input("digite seu nome")
print(f'Nome maiusculo: {nome.upper()}')
print(f'Nome minusculo: {nome.lower()}')
print(f'Tamananho do nome sem os espaços: {len(nome.replace(" ",""))}')
posicao = nome.find(' ')
print(posicao)
fNome = nome[:posicao]
print(fNome)
print(f'Tamanha do primeiro nome {posicao - 1}')
print((nome.split()))
nome = input("digite seu nome: ")'''



'''23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos 
separados. Exemplo:
digite um número: 1834
respostas: unidade: 4, dezena 3, centena 8 e milhar 1.
n = input(('Digite um numero de 1 a 9999: '))

if len(n) == 4:
    print(f'milhar: {n[0]}')
    print(f'centena: {n[1]}')
    print(f'dezena: {n[2]}')
    print(f'unidade: {n[3]}')
elif len(n) == 3:
    print(f'centena: {n[0]}')
    print(f'dezena: {n[1]}')
    print(f'unidade: {n[2]}')
elif len(n) == 2:
    print(f'dezena: {n[0]}')
    print(f'unidade: {n[1]}')
elif len(n) == 1:
    print(f'unidade: {n[0]}')'''




'''24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 
“SANTO”.
cidade = input('Digite o nome da sua cidade: ')
cidade.upper()
print(cidade.find('SANTO'))'''


'''25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem “silva” no nome.'''
nome = input('digite seu nome: ')
busca = nome.find('silva')
print(busca)
if busca != -1:
    print('Tem silva no nome')
else:
    print('Não tem silva no nome')

'''26 - Faça um programa que leia uma frase e retorne: - Quantas vezes aparece a letra “a”. - 
Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.'''

# frase = input('digite uma frase: ')
# print(f'{frase.count("a")}')
# print(frase.find('a'))
#
#
# '''27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.'''
# noma = input('Nome: ')


# frase ='Romário Paixão'
# print(frase.split())
# print('-'.join(frase))
# # print(frase.rstrip().lstrip())
# # print(f'o tamanho da frase é:',len(frase))
# # print(frase[9::3])


# frase = 'Curso em Video Python'
# print(len(frase))
# print(frase[:21]