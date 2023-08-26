from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.youtube.com')
sleep(3)
navegador.find_element('xpath', '//*[@id="search"]').send_keys('don l favela venceu')
sleep(3)
navegador.find_element('xpath', '//*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div').click()
navegador.find_element('')
# //*[@id="search"] #search
# //*[@id="search-icon-legacy"]/yt-icon/yt-icon-shape/icon-shape/div #btnSearch

sleep(5)