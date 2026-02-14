"""Open closed principle, code should open for extension ,without changing the existing code """


from abc  import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("paid with upi")

class CARD(Payment):
    def pay(self):
        print("paid with card");


if __name__=="__main__":
    upi=UPI()
    upi.pay()

    card=CARD()
    card.pay()   
    
    """ if we want to add cash option, we can create cash class and add to keep open-closed principle """