# Import libs
import chromedriver_autoinstaller as chromedriver
import chromedriver_binary

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url = "https://curso-python-selenium.netlify.app/exercicio_02.html"

# Set browser
browser = Chrome()

# Maximizing window
browser.maximize_window()

# wait for 20 seconds
browser.implicitly_wait(5)

# Open site
browser.get(url)

p = browser.find_elements(By.TAG_NAME, "p")
a = browser.find_element(By.TAG_NAME, "a")

for i in range(2):
    
    p = browser.find_elements(By.TAG_NAME, "p")

    if 'Numero esperado: ' in p[i].text:
        
        win_value = p[i].text[-1]
        print(f'Valor para ganhar: {win_value}')
    else:
        print("")

x = True
c = 1

while x == True:

    a.click()
    value_a = browser.find_elements(By.TAG_NAME, "p")

    c = c + 1

    if win_value == value_a[c].text[-1]:             

        print(f'{c} Valor esperado {win_value} encontrado, valor encontrado {value_a[1].text[-1]}')

        # Wait for 20 seconds
        sleep(20)

        # Browser closed after sleep
        browser.quit()

    else:
        print(f'{c} Valor esperado {win_value} não encontrado, valor encontrado {p[i].text[-1]}')
