# Задание №1

val = 158
name_list = 'Катя', 'Вася', 'Петя'

print(val)
print(name_list)

name = input('Как вас зовут? ')
date = input('Введите дату вашего рождения ')

print('Вас зовут ', name)
print('Вы родились ', date)

# Задание №2

data = int(input('Введите количество секунд '))
seconds = '0%s' % str(data % 60) if data % 60 < 10 else data % 60
minuts = '0%s' % str((data // 60) % 60) if (data // 60) % 60 < 10 else (data // 60) % 60
hours = '0%s' % str(data // 3600) if data // 3600 < 10 else data // 3600
print('Ответ: %s:%s:%s' % (hours, minuts, seconds))


# Задание №3

data = input('Введите число от 1 до 9 ')
print(int(data) + int(data*2) + int(data*3))

# Задание №4

data = input('Введите число ')
k = 1
g = data[0]
while k < len(data):
    g = data[k] if g < data[k] else g
    k += 1
print('Самая большая цифра в числе - ', g)

# Задание №5

v = int(input('Введите выручку фирмы '))
i = int(input('Введите издержки фирмы '))
if v > i:
    print('Фирма работает в прибыль. Прибыль составила %s' %(v - i))
    s = int(input('Введите количество сотрудников работающих на фирме '))
    print('Прибыль фирмы в расчете на одного сотрудника составила %s' %((v - i) / s))
else:
    print('Фирма работает в убыток. Убыток составил %s' %(v-i))

# Задание №6

a = 2  # растояние которое пробежал спортсмен в первый день
b = 3  # требуемое растояние
day = 1
while True:
    print('%.2f' %a, day)
    if a > b:
        break
    a = a * 1.1
    day += 1
print('Ответ: на %s-й день спортсмен достиг результата — не менее %s км.' %(day, b))

