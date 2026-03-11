class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.__fined = False # оштрафован
        self.__max_speed = 100

    def _test(self):
        print(f"Test car color:{self.color}, {self.__fined}")

    def __test2(self):
        print(f"Test private method {self.__max_speed}")

    def drive_to(self, destination):
        if not self.__fined:
            print(f"Машина {self.model} едет в {destination}, max speed {self.__max_speed}")
            self.__test2()
        else:
            print("Машина оштрафована")

    def change_color(self, new_color):
        self.color = new_color

    def fine(self):
        self.__fined = True

    def pay_fine(self):
        self.__fined = False

    # геттер - getter
    def get_max_speed(self):
        return self.__max_speed

    # сеттер - setter
    def set_max_speed(self, new_speed):
        if new_speed <= 0:
            raise ValueError(f"wrong value {new_speed} for max_speed")
        self.__max_speed = new_speed

    def set_fined(self, value):
        self.__fined = value

    # геттер
    @property
    def max_speed(self):
        return self.__max_speed

    # сеттер
    @max_speed.setter
    def max_speed(self, value):
        print(f" в сеттере {value}")
        if value <= 0:
            raise ValueError(f"wrong value {value} for max_speed")
        self.__max_speed = value


car_mustang = Car(color='black', model='Ford Mustang')
car_mustang._test()
print(car_mustang.color)
car_mustang.drive_to('Karakol')
print(car_mustang._Car__max_speed) # нельзя оставлять такой код, это просто для проверок
# print(car_mustang.__max_speed) # ошибка - доступ к приватному атрибуту
# car_mustang.__test2()
car_mustang.__max_speed = 50 # так делать неправильно, может привести к ошибкам
car_mustang.drive_to('Karakol')
# задание:
car_mustang.fine() # сделать метод чтобы штрафовать машину
car_mustang.drive_to('Karakol') # не едет, т.к. оштрафовали
print("----")
car_mustang.pay_fine() # чтобы снимать штраф
car_mustang.drive_to('Karakol')
print("--- max speed ---")
print(car_mustang.get_max_speed())
car_mustang.set_max_speed(101)
print(car_mustang.get_max_speed())

print(car_mustang.max_speed)
car_mustang.max_speed = -100
print(car_mustang.max_speed)

class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        ...



