class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def display_details(self):
        return (f"Name : {self.name} \n Age : {self.age} \n Marks : {self.marks}\n")

if __name__=="__main__":
    student1= Student("tharun",23,75)
    print(student1.display_details())

    student2= Student("virat",25,90)
    print(student2.display_details())
    
    student3=Student("rohit",26,98)
    print(student3.display_details())