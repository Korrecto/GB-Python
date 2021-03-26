# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

print('Вариант 1')  #########################################################

file = open("file_less_5_2.txt", "r", encoding="utf-8")
strings = 0
while True:
    text = file.readline().split()
    if len(text) == 0:
        break
    print(text)
    print('Количество слов в строке -', len(text))
    strings += 1
file.close()
print(f'Всего строк в файле {strings}')


print('Вариант 2')  ##########################################################

with open('file_less_5_2.txt', encoding='utf-8') as f:
    file = f.readlines()
    strings = 0
    for ff in file:
        print(ff.split())
        print('Количество слов в строке -', len(ff.split()))
        strings += 1
    print(f'Всего строк в файле {strings}')
