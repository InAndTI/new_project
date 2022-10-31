from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from time import sleep


def translate(en_word):
    try:
        url = f"https://translate.google.com/?hl=ru&sl=auto&tl=ru&text={en_word}&op=translate"
        driver = webdriver.Chrome()
        driver.get(url)
        sleep(1)
        try:
            ru_word = driver.find_element(By.CLASS_NAME, "ryNqvb")
            a = ru_word.text
        except NoSuchElementException:
            try:
                sleep(5)
                ru_word = driver.find_element(By.CLASS_NAME, "ryNqvb")
                a = ru_word.text
            except NoSuchElementException:
                driver.close()
                return "плохой интернет"
        driver.close()
        return a
    except WebDriverException:
        return "нет интернета"