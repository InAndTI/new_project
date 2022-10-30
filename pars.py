from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

en_word = "run"
url = f"https://translate.google.com/?hl=ru&sl=auto&tl=ru&text={en_word}&op=translate"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# ru_word = soup.find('div', class_="QFw9Te")
# print(ru_word)
driver = webdriver.Chrome()
driver.get(url)
print(1)
ru_word = driver.find_element(By.CLASS_NAME, "ryNqvb")
print(ru_word.text)
driver.close()