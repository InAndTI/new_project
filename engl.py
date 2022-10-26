import random
from word import *

ERROR = []

k = 0
print('ошибок:', k)
while len(words_eng_1 or eng_sych):
    if len(words_eng_1):
        i = random.randint(0, len(words_eng_1) - 1)
        print(words_rus[i])
        eng1 = input('1:')
        eng2 = input('2:')
        if words_eng_1[i] == eng1 and words_eng_2[i] == eng2:
            words_eng_2.remove(words_eng_2[i])
            words_eng_1.remove(words_eng_1[i])
            words_rus.remove(words_rus[i])
            print('осталось:', len(words_rus) + len(rus_sych))
        else:
            print(words_eng_1[i])
            print(words_eng_2[i])
            ERROR.append([words_rus[i], [eng1, words_eng_1[i]], [eng2, words_eng_2[i]]])
            k += 1
    if len(eng_sych):
        i = random.randint(0, len(eng_sych) - 1)
        print(rus_sych[i])
        eng1 = input('1:')
        if eng_sych[i] == eng1:
            eng_sych.remove(eng_sych[i])
            rus_sych.remove(rus_sych[i])
            print('осталось:', len(words_rus) + len(rus_sych))
        else:
            print(eng_sych[i])
            ERROR.append([rus_sych[i], [eng1, eng_sych[i]]])
            k += 1

print('ошибок:', k)
for i in ERROR:
    print(i)