#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
# состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

print('Вариант 1')

def int_func(a):
    return a.capitalize()


print(int_func('нижний'))
print(int_func('регистр'))

text2 ='Каждое слово состоит из латинских букв в нижнем регистре.'
text3 = text2.split(' ')
text4 = ''
for t in text3:
    text4 += int_func(t) + ' '
print(text4)



print('вариант 2')

def int_func2(a):
    return a.title()


print(int_func2('нижний'))
print(int_func2('регистр'))
text2 ='Каждое слово состоит из латинских букв в нижнем регистре.'
print(int_func2(text2))
