
words_rus = 'быть иметь сказать идти получать делать знать думать брать видеть приходить хотеть использовать находить давать рассказывать работать звонить пытаться просить нуждаться чувствовать становиться оставлять класть значить хранить позволять начинать казаться помогать показывать слышать играть бежать двигаться жить верить приносить случаться писать сидеть стоять терять платить встречать включать продолжать устанавливать изучать менять вести понимать смотреть следовать останавливать создавать говорить читать тратить расти открывать гулять побеждать учить предлагать помнить считать появляться покупать служить умирать посылать строить оставаться падать резать достигать убивать поднимать миновать продавать решать возвращаться объяснять надеяться развивать нести ломать соглашаться поддерживать ударять производить есть покрывать ловить рисовать выбирать напоминать запрещать благодарить снабжать добавлять прыгать плавать любить обсуждать избегать забывать зависеть переводить одобрять готовить учиться улыбаться повторять присоединять заканчивать планировать танцевать носить ехать отменять лежать плакать пить навещать водить желать петь летать держать болтать бояться кричать поворачивать слушать соединять путешествовать'.split(' ')
words_eng_1 = 'be have say go get make know think take see come want use find give tell work call try ask need feel become leave put mean keep let begin seem help show hear play run move live believe bring happen write sit stand lose pay meet include continue set learn change lead understand watch follow stop create speak read spend grow open walk win teach offer remember consider appear buy serve die send build stay fall cut reach kill raise pass sell decide return explain hope develop carry break agree support hit produce eat cover catch draw choose remind prohibit thank provide add jump swim love discuss avoid forget depend translate approve cook study smile repeat join end plan dance wear ride cancel lie cry drink visit drive wish sing fly hold talk fear shout turn listen connect travel'.split(' ')
words_eng_2 = 'were had said went got made knew thought took saw came wanted used found gave told worked called tried asked needed felt became left put meant kept let began seemed helped showed heard played ran moved lived believed brought happened wrote sat stood lost paid met included continued set learned changed led understood watched followed stopped created spoke read spent grew opened walked won taught offered remembered considered appeared bought served died sent built stayed fell cut reached killed raised passed sold decided returned explained hoped developed carried broke agreed supported hit produced ate covered caught drew chose reminded prohibited thanked provided added jumped swam loved discussed avoided forgot depended translated approved cooked studied smiled repeated joined ended planned danced wore rode cancelled lay cried drank visited drove wished sang flew held talked feared shouted turned listened connected travelled'.split(' ')
eng_sych = 'as for on with from by hot word other time air well also small end home hand here must big high such light kind picture again animal point mother world near father new part place after back little only round year good under name very through just sentence great low line cause before right boy old there up way about then would like so long thing more day number sound water may down side now head own page country answer still plant food sun between eye never last city tree hard story far sea left late while night real life few book science room friend idea fish mountain once horse sure colour face main together next white children example ease paper group always music both mark often river car feet second enough plain girl usual young ready red list bird soon body dog family door black short wind question complete ship half rock order fire problem top street multiply nothing full'.split(' ')
rus_sych = 'как для на с из от горячий слово другой время воздух хорошо также маленький конец дом рука здесь должен большой высокий такой свет\легкий добрый картина снова животное точка мать мир близко отец новый часть место после назад немного только круглый год хороший под имя очень через только\просто предложение отличный низкий линия причина до право мальчик старый там вверх путь о затем бы нравиться так длинный вещь больше день номер звук вода может вниз сторона сейчас голова свой страница страна ответ все.еще растение еда солнце между глаз никогда последний город дерево тяжелый история далеко море лево поздно пока ночь реальный жизнь несколько книга наука комната друг идея рыба гора однажды лошадь конечно цвет лицо главный вместе следующий белый дети пример легкость бумага группа всегда музыка оба отметка часто река машина ноги секунда хватает простой девочка обычно молодой готовый красный список птица скоро тело собака семья дверь черный короткий ветер вопрос завершенный корабль половина камень приказ огонь проблема верх улица умножать ничего полный'.split(' ')

c = words_rus
b = rus_sych
a = set(b)
for i in b:
    if b.count(i) > 1:
        print(i)
for i in c:
    if c.count(i) > 1:
        print(i)
print(len(words_rus))
print(len(words_eng_1))
print(len(words_eng_2))
print(len(eng_sych))
print(len(rus_sych))
print(1)

