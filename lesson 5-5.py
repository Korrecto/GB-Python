# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random
# запись в файл
with open("Write_less_5_5.txt", "w", encoding="utf-8") as file:
    file.write(" ".join([str(random.randint(0, 99)) for i in range(20)]))
# чтение и сложение
with open("Write_less_5_5.txt", "r", encoding="utf-8") as obj:
    my_list = obj.read()
    print(my_list)
    print(sum([int(i) for i in my_list.split()]))
