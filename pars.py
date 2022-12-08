from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from time import sleep


def translate(en_word: str):
    en_word = en_word.split(' ')
    for i in range(len(en_word) - 1):
        en_word[0] += '%20' + en_word[i + 1]
    en_word = en_word[0]
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
        get(a, en_word)
        return a
    except WebDriverException:
        return "нет интернета"


def get(ru, en):
    from mysql.connector import connect, Error
    try:
        with connect(
            host="localhost",
            user="root",
            password="3102032Vit",
            database="word_1000",
        ) as connect:
            insert_movies_query = f"""
            INSERT INTO the_word (ru_word, en_word)
            VALUES
                ("{ru.lower()}","{en}")
            """
            with connect.cursor() as cursor:
                cursor.execute(insert_movies_query)
                connect.commit()
        copy()
    except Error:
        print(Error)


def copy():
    from mysql.connector import connect, Error
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