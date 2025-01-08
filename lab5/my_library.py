def task5_1(word1, word2):
    '''
    Даны два слова (первое длиннее второго). Заменить во втором слове
    соответствующее количество символов на первое слово.

    :param word1: первое слово
    :param word2: второе слово
    :return: новое слово или ошибка
    '''

    # Проверяем, что первое слово длиннее второго
    if len(word1) > len(word2):
        # Заменяем символы во втором слове на первое слово
        new_word2 = word1 + word2[len(word1):]
        return new_word2
    else:
        return "Ошибка: Первое слово должно быть длиннее второго."


def task5_2(text):
    '''
    Дан текст из слов, разделенных знаками препинания. Получить список слов
    текста, у которых первая и последняя буквы совпадают. Каждое слово
    выводит один раз (независимо от количества вхождений)

    :param text: вводимый текст
    :return: результат
    '''

    # Заменяем знаки препинания на пробелы и разбиваем текст на слова
    words = text.replace(',', ' ').replace('.', ' ').replace(':', ' ').split()

    # Множество для хранения уникальных слов
    unique_words = set()

    # Проходим по каждому слову
    for word in words:
        # Проверяем, что слово не пустое и первая буква совпадает с последней
        if len(word) > 0 and word[0].lower() == word[-1].lower():
            unique_words.add(word)
    # Сортируем
    result = sorted(unique_words)

    return result


def task5_3(text):
    '''
    Дана строка символов, состоящая из произвольного текста, слова разделены
    пробелами. Вывести на экран порядковый номер слова максимальной длины
    и номер позиции строки с которой оно начинается.

    :param text: вводимый текст
    :return: None
    '''

    words = text.split()

    max_length = 0
    max_index = -1

    for index, word in enumerate(words):
        # Если длина текущего слова больше максимальной
        if len(word) > max_length:
            max_length = len(word)
            max_index = index

    # Находим позицию начала слова в строке
    if max_index != -1:
        start_position = text.find(words[max_index])
        print("Порядковый номер слова максимальной длины:", max_index + 1)
        print("Номер позиции строки, с которой оно начинается:", start_position)
    else:
        print("Нет слов в строке.")


def task5_4(text):
    '''
    В тексте нет слов, начинающихся одинаковыми буквами. Напечатать слова
    текста в таком порядке, чтобы последняя буква каждого слова совпадала с
    первой буквой последующего слова. Если все слова нельзя напечатать в
    таком порядке, найти такую цепочку, состоящую из наибольшего количества слов.

    :param text: вводимый текст
    :return: None

    '''
    words = text.split()

    # Список для хранения цепочки слов
    new_text = []

    # Начинаем с первого слова
    current_word = words[0]
    new_text.append(current_word) # Добавляем первое слово в цепочку
    words.remove(current_word) # Удаляем первое слово из списка оставшихся слов

    while True:
        found = False # Флаг для отслеживания, найдено ли слово
        for word in words:
            if current_word[-1] == word[0]:  # Проверяем совпадение последней и первой буквы
                new_text.append(word)
                current_word = word
                words.remove(word) # Удаляем найденное слово из списка оставшихся
                found = True
                break
        if not found:  # Если не нашли подходящее слово, выходим из цикла
            break

    print("Цепочка слов:", ' -> '.join(new_text))


def task5_5(input_string):
    '''
    Написать регулярное выражение, определяющее является ли данная строка
    GUID с или без скобок. Где GUID это строчка, состоящая из 8, 4, 4, 4, 12
    шестнадцатеричных цифр, разделенных тире.
    – пример правильных выражений: e02fd0e4-00fd-090A-ca30-0d00a0038ba0
    – пример неправильных выражений: e02fd0e400fd090Aca300d00a0038ba0

    :param input_string:
    :return: None
    '''

    import re

    guid_pattern = r'^\{?([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})\}?$'

    if re.match(guid_pattern, input_string):
        print("Строка является корректным GUID.")
    else:
        print("Строка не является корректным GUID.")


def task5_6(input_string):
    '''
    Строки, содержащие «cat» в качестве слова. Пример строк, которые
    подходят: «cat», «catapult and cat», «catapult and cat and concatenate». Пример
    строк, которые не подходят: «catcat», «concat», «Cat».

    :param input_string: вводимая строка
    :return: результат
    '''
    import re

    pattern = r'\bcat\b'

    if re.search(pattern, input_string):
        return "Строка содержит 'cat' как отдельное слово."
    else:
        return "Строка не содержит 'cat' как отдельное слово."


def task5_7(input_string):
    '''
    Заменить все вхождения слова «human» на слово «computer». Запрещается
    использовать обратные ссылки. Указание: используйте «\b». Примеры замен:
    «I need to understand the human mind» → «I need to understand the computer
    mind», «humanity» → «humanity».

    :param input_string: вводимая строка
    :return: измененная строка
    '''
    import re

    output_string = re.sub(r'\bhuman\b', 'computer', input_string)

    return output_string






