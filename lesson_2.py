# родительский, суперкласс, parent class
class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Машина {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color


# дочерний класс, подкласс, child class
class Bus(Car):
    def __init__(self, color, model, seat_number):
        super().__init__(color, model)
        self.seat_number = seat_number

    def drive_to(self, destination):
        super().drive_to(destination)
        print(f"Автобус {self.model} едет в {destination}")


class Minibus(Bus):
    pass


class Truck(Car):
    def __init__(self, color, model, max_weight, seat_number):
        super().__init__(color, model)
        self.max_weight = max_weight
        self.seat_number = seat_number


car_mustang = Car(color='black', model='Ford Mustang')
bus_40 = Bus(color='green', model='Mercedes Benz', seat_number='40',)
print(bus_40.color, bus_40.model)
bus_40.drive_to("Bishkek")

print("Type of bus", type(bus_40))
print("Type of car", type(car_mustang))
print(isinstance(bus_40, Bus))
print(isinstance(bus_40, Car))


vehicles = [bus_40, car_mustang]
for v in vehicles:
    v.drive_to(destination="Kant")