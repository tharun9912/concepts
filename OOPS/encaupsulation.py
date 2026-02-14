
# encapsulation,wrapping of variables and methods and preventing direct access of data.   

class Person:
    def __init__(self,name,salary=0):
        self.__name=name        # private variable
        self.__salary=salary    # private variable , only objects can access those variables.

    def set_salary(self,amount):
        self.__salary+=amount

    def get_salary(self):
        return self.__salary
    
if __name__=="__main__":
    person= Person("tharun")
    person.set_salary(15000)
    print(person.get_salary())

    
