class Car:
    # инициализатор(конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Машина {self.model} едет в {destination}")

    def change_color(self, new_color):
        self.color = new_color

car1 = Car(color='black', model='Ford Mustang')
car2 = Car(color='silver', model='Subaru Forester')
print("Car 1:", car1.color, car1.model)
print("Car 2:", car2.color, car2.model)
print(type(1233))
print(type(car1))
car1.drive_to("Бишкек")
car1.color = "red"
print("Car 1:", car1.color, car1.model)
car1.change_color("white")
print("Car 1:", car1.color, car1.model)
car1.max_speed = 240
print("Car 1:", car1.max_speed, car1.model)
# print(car2.max_speed)
