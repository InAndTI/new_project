from bs4 import BeautifulSoup
import requests


en_word = "run"
url = f"https://translate.google.com/?hl=ru&sl=auto&tl=ru&text={en_word}&op=translate"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
ru_word = soup.find('div', class_="QFw9Te")
print(ru_word)