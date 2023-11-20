#[PY-A05]Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.
def media_valores(lista: list) -> int or float:
    soma = sum(lista)
    media = soma / len(lista)

    return media

lista_numeros = [1, 2, 3 ,4 ,5 ,6]


print(f"A media das notas é {media_valores(lista_numeros)}")