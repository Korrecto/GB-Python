# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо
# написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

file = open("file_less_5_4.txt", "r", encoding="utf-8")
new_file = open("Write_file_less_5_4.txt", "w", encoding="utf-8")
while True:
    text = file.readline().split()
    if len(text) == 0:
        break
    text[0] = my_dict[text[0]]
    new_file.write(" ".join(text) + '\n')
file.close()
new_file.close()
