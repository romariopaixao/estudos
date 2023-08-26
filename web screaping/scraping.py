from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#abrindo o webdrive do chorme na variavel navegador
navegador = webdriver.Chrome()

#variavel navegador com o metodo get de entrar na url
navegador.get('https://www.youtube.com/')
sleep(3)
search = navegador.find_element(By.ID, 'search')

search.send_keys('asd')



# print(buttonCarro)


# <div class="title">