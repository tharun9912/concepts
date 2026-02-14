""" Interface segregation principle, no class should forced to implement unused methods """

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass


# Human needs both
class Human(Workable, Eatable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


# Robot needs only Workable,if we force robot to eat,then it will violate interface segregation principle.

class Robot(Workable):
    def work(self):
        print("Robot working")


if __name__ == "__main__":
    human = Human()
    robot = Robot()

    human.work()
    human.eat()

    robot.work()
