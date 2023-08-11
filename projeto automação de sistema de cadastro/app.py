import pyautogui
from time import sleep

# 1- Clicar e digitar meu usuario
pyautogui.click(981,538,duration=0.1)
pyautogui.write('jhonatan')

# 2- Clicar e digitar minha senha
pyautogui.click(973,568,duration=0.1)
pyautogui.write('123456')

# 3- Clicar em entrar
pyautogui.click(867,597,duration=0.1)

# 4- Extrair cada produto
with open('produtos.txt','r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
    #     1- Clica e digitar produto
        pyautogui.click(688,527,duration=0.1)
        pyautogui.write(produto)
    #     2- Clicar e digitar quantidade
        pyautogui.click(683,555,duration=0.1)
        pyautogui.write(quantidade)
    #     3- Clicar e digitar preco
        pyautogui.click(682,586,duration=0.1)
        pyautogui.write(preco)
    #     4- Clicar em registrar
        pyautogui.click(598,738,duration=0.1)
        sleep(1)