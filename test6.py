# Inner/Nested classes example:

class Person:
    def __init__(self,name,dd,mm,yy):
        self.name=name
        self.dob=self.DOB(dd,mm,yy)
    def disply(self):
        print('Rahul')
        self.dob.dispaly()
    class DOB:
        def __init__(self,dd,mm,yy):
            self.dd=dd
            self.mm=mm
            self.yy=yy
            print('Indside class constructor')
        def dispaly(self):
            print("DOB is {}/{}/{}.".format(self.dd,self.mm,self.yy))

p1=Person('rahul',17,3,1999)
p1.disply()