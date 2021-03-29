# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение.'

    def stop(self):
        return f'остановился.'

    def turn(self, direction):
        return f' повернул {direction}'

    def show_speed(self):
        return f'\nСо скоростью {self.speed} км/ч.'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nСкорость превышена, значение {self.speed} км/ч.'
        else:
            return f'Скорость {self.name} допустимая'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nСкорость превышена, значение {self.speed} км/ч.'
        else:
            return f'Скорость {self.name} допустимая'

class PoliceCar(Car):
    pass


town = TownCar('Киа', 70, 'blue', False)
print(town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop())

sport = SportCar('Ламба', 170, 'red', False)
print(sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Газель', 30, 'red', False)
print(work.go(), work.show_speed(), work.turn('налево'), work.stop())

police = PoliceCar('Форд', 100, 'бело/синий', True)
print(police.go(), police.show_speed(), police.turn('направо'), police.stop())
