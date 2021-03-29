# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Отрисовка {self.title}')



item_1 = Pen('карандашом')
item_1.draw()

item_2 = Pencil('ручкой')
item_2.draw()

item_3 = Handle('маркером')
item_3.draw()
