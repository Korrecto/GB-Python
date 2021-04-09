# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, val):
        self.val = val


def func():
    try:
        val1 = int(input('Введите делимое число: '))
        val2 = int(input('Введите число делитель: '))
        if val2 == 0:
            raise OwnError("ERROR! Делить на ноль нельзя")
        else:
            result = val1 / val2
            return result
    except ValueError:
        return "Вы ввели не число"
    except OwnError as e:
        return e


print(func())
