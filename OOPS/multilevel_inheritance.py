 
""" Multilevel inheritance, a class inherits from a class,and another class inherits from that derived class. """

class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("dog barks")

class Puppy(Dog):
    def weep(self):
        print("puppy weeps softly")

if __name__== "__main__":
    
    p=Puppy()

    p.eat()
    p.bark()
    p.weep()