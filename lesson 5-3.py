# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.

from statistics import mean

with open('file_less_5_3.txt', encoding='utf-8') as f:
    file = f.readlines()
    staff = []
    average = []
    for ff in file:
        average.append(float(ff.split()[1]))
        if float(ff.split()[1]) < 20000:
            staff.append(ff.split()[0])

    print('Список сотрудников чей оклад менее 20 тыс. -', staff)
    print('Cредняя величина дохода сотрудников -', round(mean(average), 2))
