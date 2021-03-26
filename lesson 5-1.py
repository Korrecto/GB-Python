# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.


with open("Write_less_5_1.txt", "w", encoding="utf-8") as file:
    while True:
        my_list = input('Введите строку ')
        if my_list == '':
            break
        file.write(my_list + '\n')
