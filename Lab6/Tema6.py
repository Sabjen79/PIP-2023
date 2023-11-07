import math

# Ex1
class Shape:
    def __init__(self, s):
        self.size = s

class Circle(Shape):
    def area(self):
        return math.pi * (self.size**2)
    
    def perimeter(self):
        return 2*math.pi*self.size
    
class Square(Shape):
    def area(self):
        return self.size**2
    
    def perimeter(self):
        return 4*self.size
    
class Triangle(Shape):
    def area(self):
        return math.sqrt(3)/4*(self.size**2)
    
    def perimeter(self):
        return 3*self.size
    
a = Circle(1)
print(a.area())

#Ex 2
class Account:
    def __init__(self, money):
        self.balance = money
    
    def deposit(self, x):
        self.balance += x

    def withdraw(self, x):
        self.balance -= x

    def interest(self):
        return 0

class SavingsAccount(Account):
    def interest(self):
        return 0.1*self.balance
    
class CheckingAccount(Account):
    def interest(self):
        return 0.3*self.balance
    
b = SavingsAccount(10)
b.deposit(10)
print(b.interest())

#Ex 3
class Vehicle:
    def __init__(self, make, model, year, capacity, power):
        self.make = make
        self.model = model
        self.year = year
        self.capacity = capacity
        self.power = power

    def mileage(self):
        return self.capacity*100
    
    def towing_capacity(self):
        return self.power

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, 40, 100)

class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, 20, 40)

class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year, 100, 300)

c = Truck("Iveco", "200D", 2012)
print(c.mileage())

#Ex 4
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 3000)
        self.team = []

    def add_to_team(self, employee):
        self.team.append(employee)

    def remove_from_team(self, employee):
        self.team.remove(employee)

class Engineer(Employee):
    def __init__(self, name):
        super().__init__(name, 1000)
        self.projects = []

    def add_to_projects(self, project):
        self.projects.append(project)

    def remove_from_projects(self, project):
        self.projects.remove(project)

class Salesperson(Employee):
    def __init__(self, name):
        super().__init__(name, 2000)
        self.sales = []

    def add_to_sales(self, sale):
        self.sales.append(sale)

    def remove_from_sales(self, sale):
        self.sales.remove(sale)

d = Manager("Geta")
d.add_to_team("Augustin")
print(d.team)

#Ex 5
class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
    
    def eat(self, calories):
        self.weight += calories*0.1

class Bird(Animal):
    def __init__(self, name, songs):
        super().__init__(name)
        self.songs = songs
    
    def learn_song(self):
        self.songs += 1

class Fish(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def change_color(self, color):
        self.color = color

e = Bird("Aslan", 5)
e.learn_song()
print(e.songs)

#Ex 6
class LibraryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.bought = False

    def check_out(self):
        self.bought = True

    def return_item(self):
        self.bought = False
        self.price = self.price * 0.9
    
    def display(self):
        print( f"Name: {self.name}; Price: {self.price}; Available for buying: {not self.bought}" )
    
class Book(LibraryItem):
    def __init__(self, name):
        super().__init__(name, 10)

class DVD(LibraryItem):
    def __init__(self, name):
        super().__init__(name, 5)

class Magazine(LibraryItem):
    def __init__(self, name):
        super().__init__(name, 7)

f = Book("LOTR")
f.check_out()
f.display()
f.return_item()
f.display()