# 1.Инкапсуляция
class Person:
    # Конструктор класса, инициализирует атрибуты объекта
    def __init__(self, age=0):
        self._age = 0     # Инициализация возраста
        self.set_age(age) # Установка возраста с проверкой через метод

    # Метод для установки возраста
    def set_age(self, age):
        if age < 0:  # Проверка на отрицательное значение
            raise ValueError("Возраст не может быть отрицательным.")
        self._age = age

    # Метод для получения возраста
    def get_age(self):
        return self._age

# Пример использования:
try:
    p = Person()        # Создание объекта без параметров
    p.set_age(25)       # Установка возраста
    print(p.get_age())  # Вывод: 25

    p.set_age(-5)       # Попытка установить отрицательный возраст
except ValueError as e:
    print(e)  # Вывод: Возраст не может быть отрицательным.

#2. Наследование
class Animal:
    def __init__(self, name):
        self.name = name  # Атрибут name для всех животных

    def speak(self):
        return "I am an animal"  # Метод по умолчанию для всех животных

# Класс Dog, наследующий от Animal
class Dog(Animal):
    def speak(self):
        return "Woof"  # Переопределенный метод speak для собаки

# Класс Cat, наследующий от Animal
class Cat(Animal):
    def speak(self):
        return "Meow"  # Переопределенный метод speak для кошки

# Пример использования:
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow

#3. Полиморфизм
class Vehicle:
    def move(self):
        return "Vehicle is moving"  # Общий метод для всех видов транспорта

# Класс Car, наследующий от Vehicle
class Car(Vehicle):
    def move(self):
        return "Car is driving"  # Переопределенный метод для машины

# Класс Bicycle, наследующий от Vehicle
class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"  # Переопределенный метод для велосипеда

# Функция move(), которая вызывает метод move у переданного объекта
def move(vehicle):
    return vehicle.move()

# Пример использования:
car = Car()
bike = Bicycle()

print(move(car))  # Вывод: Car is driving
print(move(bike))  # Вывод: Bicycle is pedaling

#4. Абстракция
from abc import ABC, abstractmethod
import math


# Абстрактный класс Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Абстрактный метод, который должны реализовать наследники

# Класс Rectangle, наследующий от Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width  # Ширина прямоугольника
        self.height = height  # Высота прямоугольника

    def area(self):
        return self.width * self.height  # Площадь прямоугольника

# Класс Circle, наследующий от Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius  # Радиус окружности

    def area(self):
        return math.pi * (self.radius ** 2)  # Площадь круга

# Пример использования:
rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94

