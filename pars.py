from selenium import webdriver
from selenium.webdriver.common.by import By


def translate(en_word):
    url = f"https://translate.google.com/?hl=ru&sl=auto&tl=ru&text={en_word}&op=translate"
    driver = webdriver.Chrome()
    driver.get(url)
    ru_word = driver.find_element(By.CLASS_NAME, "ryNqvb")
    print(ru_word.text)
    driver.close()

