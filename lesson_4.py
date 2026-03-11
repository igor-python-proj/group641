from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав гав")

    def test(self):
        print("тест собака")

puppy = Dog()
puppy.make_sound()