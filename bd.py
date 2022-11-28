import random


def the_word(start, amount):
    from mysql.connector import connect, Error


    def copy_front(id, word):
        sms = f"SELECT * FROM the_word WHERE id = {id}"
        with connect.cursor() as cursor:
            cursor.execute(sms)
            res = cursor.fetchall()[0]
            word.append(res[2])
            if res[3]:
                copy_front(res[3], word)


    def copy_back(id, word):
        sms = f"SELECT * FROM the_word WHERE copy_id = {id}"
        with connect.cursor() as cursor:
            cursor.execute(sms)
            res = cursor.fetchall()
            if len(res):
                word.append(res[0][2])
                copy_back(res[0][0], word)



    word_dict = {}
    try:
        with connect(
            host="localhost",
            user="root",
            password="3102032Vit",
            database="word_1000",
        ) as connect:
            select_movies_query = f"SELECT * FROM the_word LIMIT {start}, {amount}"
            with connect.cursor() as cursor:
                cursor.execute(select_movies_query)
                result = cursor.fetchall()
                for row in result:
                    if not row[1] is word_dict.keys():
                        word_dict[row[1]] = [row[2]]
                        if row[3]:
                            copy_front(row[3], word_dict[row[1]])
                        copy_back(row[0], word_dict[row[1]])
    except Error:
        print(Error)
    finally:
        return word_dict



