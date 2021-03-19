
# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

print('Первый способ')

def my_func(a, b, c):
    if a + b > b + c:
        if a + b > a + c:
            return a + b
        else:
            return a + c
    elif b + c > a + c:
        return b + c
    else:
        return a + c


print(my_func(1, 2, 3))
print(my_func(5, 4, 3))
print(my_func(8, 6, 7))
print(my_func(2, 2, 2))
print(my_func(10, 20, 3))


print('Второй способ')

def my_func(a, b, c):
    list = [a, b, c]
    list.remove(min(list))
    return sum(list)



print(my_func(1, 2, 3))
print(my_func(5, 4, 3))
print(my_func(8, 6, 7))
print(my_func(2, 2, 2))
print(my_func(10, 20, 3))
