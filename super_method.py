class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Student(Person):
    def __init__(self,name,age,rollno,marks):
        '''self.name=name
        self.age=age'''#use super method constructor to improve code resuability
        super().__init__(name,age)
        self.rollno=rollno
        self.marks=marks
    def display(self):
        '''print("Name:",self.name)
        print("Age:",self.age)'''#Put all common functionalities in parent method and call super() to execute it
        super().display()
        print("Rollno:",self.rollno)
        print("Marks",self.marks)
class Teacher(Person):
    def __init__(self,name,age,salary,subject):
        '''self.name=name
           self.age=age'''  # use super method constructor to improve code resuability
        super().__init__(name, age)
        self.salary=salary
        self.subject=subject
    def display(self):
        '''print("Name:",self.name)
                print("Age:",self.age)'''  # Put all common functionalities in parent method and call super() to execute it
        super().display()
        print("Salary:",self.salary)
        print("Subject",self.subject)

s=Student('rahul',23,172,'75%')
t=Teacher('Durga',45,100000,'python')
s.display()
print("*"*60)
t.display()