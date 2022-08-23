class Declare:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        if(self.rollno>200):
            self.group=2
        else:
            self.group=1
    def info(self):

        return self.name,self.rollno,self.group

d1=Declare('rahul',123)
d2=Declare('pavi',234)
print(d1.info())
print(d2.info())