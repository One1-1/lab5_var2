"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7



def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
                word1 = input("Введите первое слово (длиннее второго): ")
                word2 = input("Введите второе слово: ")

                print(task5_1(word1, word2))

            case 2:
                text = "Какой-то пример текста, в котором слова: арка, луна, астра, рама, и другие слова тоже могут быть."

                print(task5_2(text))

            case 3:
                text = input("Введите строку: ")

                print(task5_3(text))

            case 4:
                text = "это пример текста для задачи"

                print(task5_4(text))

            case 5:
                input_string = input("Введите строку для проверки на GUID: ")

                task5_5(input_string)

            case 6:
                input_string = input("Введите строку: ")

                print(task5_6(input_string))

            case 7:
                input_string = input("Введите строку: ")

                print(task5_7(input_string))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break


