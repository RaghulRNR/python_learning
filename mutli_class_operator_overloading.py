class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def __mul__(self, other):
        return self.salary*other.days

class Timesheet:

    def __init__(self,name,days):
        self.name=name
        self.days=days

e=Employee('rahul',100)
t=Timesheet('rahul',31)

'''the first refernce variable will consider and it will search for __mul__ method ,if it is overlaoded then 
    it will execute sucessfully or it will raise error'''
print("salary=",e*t)

#prinnt(t*e),it is alo work , Only if we overload timesheet class with __mul__