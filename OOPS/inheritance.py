"""Inheritance, Dog and Cat inherit from Animal,they override the speak() method"""

class Animal:
    def speak(self):
        print("hey")

class Dog(Animal):
    def speak(self):
        print("bow bow bow")

class Cat(Animal):
    def speak(self):
        print("meow meow")

if __name__=="__main__":

    animal=Animal()
    animal.speak()

    dog=Dog()
    dog.speak()

    cat=Cat()
    cat.speak()