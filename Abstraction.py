# Abstraction –

# The process of handling complexity by hiding unnecessary information from the user
# In Python, Abstraction can be achieved by using Abstract class and Abstract methods

# Abstract class and Abstract method –

# Python by default doesn't support abstract class and abstract method, so there is a package called ABC(abstract base classes)
# by which we can make a class or method abstract.
# Abstract method is which having a declaration and doesn't have definition.
# A class is called abstract class only if it has at least one abstract method.
# When you inherit a abstract class, the child class should define all the abstract method present in parent class.
# If it is not done then child class also becomes abstract class automatically

# Import required modules
from abc import ABC, abstractmethod


# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass

    # Create concrete method
    def accelerate(self):
        print("speed up ...")

    def break_applied(self):
        print("Car stop")


# Create a child class
class Hatchback(Car):

    def printDetails(self):
        print("Brand:", self.brand);
        print("Model:", self.model);
        print("Year:", self.year);

    def Sunroof(self):
        print("Not having this feature")


# Create a child class
class Suv(Car):

    def printDetails(self):
        print("Brand:", self.brand);
        print("Model:", self.model);
        print("Year:", self.year);


    def Sunroof(self):
        print("Available")


car1 = Hatchback("Maruti", "Alto", "2022");
car1.printDetails()
car1.accelerate()







































