from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()#isntanciando o webdriver

driver.get('https://sisdocs.ambipar.com/login')#acesando um url

sleep(3)

text_box = driver.find_element(by=By.NAME, value="email")
text_box.send_keys("financeiro@rodtransportes.com.br")
sleep(3)

password_box = driver.find_element(by=By.NAME, value="password")
password_box.send_keys("roD@2023")

submit_button = driver.find_element(by=By.XPATH, value='//*[@id="form"]/div[3]/input')
submit_button.click()


sleep(5)

driver.quit()