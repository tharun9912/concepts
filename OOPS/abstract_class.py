""" Abstract class method implementation, An abstract class is a class that
 cannot be instantiated and may contain abstract methods that must be implemented 
 by child classes."""

from abc import ABC,abstractmethod

class Payment(ABC):  # ABC makes the class as abstract 

    @abstractmethod    # @abstractmethod forces child classes to implement this method 
    def pay(self,amount):
        pass

class CreditCard(Payment):

    def pay(self,amount):
        print(f"paid {amount} using credit card")

if __name__=="__main__":
    
    # p=Payment()  this will give u an error, can't create a object for abstract classes.

    c=CreditCard()
    c.pay(50000)




