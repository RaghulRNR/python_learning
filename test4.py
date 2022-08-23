#calling one class method from another:-

class Test:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display(self):
        print('{} got {} out of 500'.format(self.name, self.marks))

class execute:
    def modify(emp):
        emp.marks=emp.marks+10
        emp.display()

t1=Test('Raghul',451)
execute.modify(t1)