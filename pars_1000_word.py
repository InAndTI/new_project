from bs4 import BeautifulSoup
import requests
import re
from mysql.connector import connect, Error


def word_1000():
    url = "https://puzzle-english.com/directory/1000-popular-words"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    ru_word_trash = soup.find_all('li', style="font-weight: 400;")
    for word_trash in ru_word_trash:
        en_word = re.findall(r"[a-z]+", word_trash.text)
        ru_word = re.findall(r"[а-я][^/]*[а-я]", word_trash.text)
        a = en_word[0]
        b = ", ".join(ru_word)
        print(a, b)

def give(id, copy_id):
    update_query = f"""
    UPDATE
        the_word
    SET
        copy_id = {copy_id}
    WHERE
        id = {id}
    """
    with connect.cursor() as cursor:
        cursor.execute(update_query)
        connect.commit()


if __name__ == "__main__":
    try:
        with connect(
            host="localhost",
            user="root",
            password="3102032Vit",
            database="word_1000",
        ) as connect:
            select_movies_query = f"SELECT * FROM the_word"
            with connect.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for i, row in enumerate(result):
                    for j in range(i - 1, 0, -1):
                        if row[1] == result[j][1]:
                            give(result[j][0], row[0])
                            break
            # delete_query = "DELETE FROM the_word WHERE ru_word = """
            # with connect.cursor() as cursor:
            #     cursor.execute(delete_query)
            #     connect.commit()
    except Error:
        print(Error)




