from bs4 import BeautifulSoup
import requests
import re


url = "https://puzzle-english.com/directory/1000-popular-words"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
ru_word_trash = soup.find_all('li', style="font-weight: 400;")
for word_trash in ru_word_trash:
    en_word = re.findall(r"[a-z]+", word_trash.text)
    print(en_word[0])
    ru_word = re.findall(r"[а-я][^/]*[а-я]", word_trash.text)
    print(ru_word)
