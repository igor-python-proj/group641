class User:
    # переменные класса
    user_count = 0
    default_password = "12345678"

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.password = User.default_password
        User.user_count += 1

    def get_name(self):
        return self.name

    @classmethod
    def get_user_count(cls):
        return cls.user_count

    @classmethod
    def create_user(cls, name, phone_number):
        if not phone_number.isdigit():
            raise ValueError(f"неправильный формат телефона {phone_number}")
        new_user = cls(name, phone_number)
        return new_user


user_1 = User("Игорь", "996555000001")
user_2 = User("Курманбек", "996555000002")
print(user_1.name)
print(user_2.name)
print(user_1.password, user_2.password)
print("Кол-во пользователей", User.user_count)
User.user_count += 1
user_3 = User("Рома", "996555000003")
print("Кол-во пользователей", User.user_count)
print(User.get_user_count())
user_4 = User.create_user(name="Артур", phone_number="987654321")
print(user_4.name)
