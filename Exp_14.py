# class Car:
#     # Constructor to initialize the object
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute

#     # Method to describe the car
#     def car_details(self):
#         return f"Car: {self.brand}, Model: {self.model}"

# # Creating an object of the Car class
# my_car = Car("Hyundai", "Creta")
# print(my_car.car_details())  




# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     # Method to calculate area
#     def area(self):
#         return self.width * self.height
#     # Method to calculate perimeter
#     def perimeter(self):
#         return 2 * (self.width + self.height)
# # Create an object
# rect = Rectangle(7, 12)
# # Accessing methods
# print(f"Area: {rect.area()}")  
# print(f"Perimeter: {rect.perimeter()}")  





# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  # Private attribute

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient funds")

#     def get_balance(self):
#         return self.__balance

# # Create an account
# account = BankAccount("Devansh", 71000)
# account.deposit(500)
# print(account.get_balance())  # 
# account.withdraw(700)
# print(account.get_balance())  # 





# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "I am an animal."

# # Dog class inherits from Animal class
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"

# # Cat class inherits from Animal class
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"

# dog = Dog("Buddy")
# cat = Cat("Whiskers")
# print(dog.speak())  # 
# print(cat.speak())  # 






# class Polygon:
#     # method to render a shape
#     def render(self):
#         print("Rendering Polygon...")

# class Square(Polygon):
#     # renders Square
#     def render(self):
#         print("Rendering Square...")

# class Circle(Polygon):
#     # renders circle
#     def render(self):
#         print("Rendering Circle...")
    
# # create an object of Square
# s1 = Square()
# s1.render()

# # create an object of Circle
# c1 = Circle()
# c1.render()





# from abc import ABC, abstractmethod

# # Abstract class
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# circle = Circle(7)
# print(f"Area of the circle: {circle.area()}")  # 




#postlab
#1
# import math
# class Circle:
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return math.pi * self.r**2

#     def perimeter(self):
#         return 2 * math.pi * self.r
    
# c = Circle(7)
# print("Area:", c.area())
# print("Perimeter:", c.perimeter())





#2
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)


b1 = Book("Python Basics", "John Smith", 500)
b2 = Book("Data Science 101", "Alice Brown", 650)

b1.display()
b2.display()

b1.apply_discount(10)
print("\nAfter 10% discount on first book:")
b1.display()
