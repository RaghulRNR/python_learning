class Test:
    cname='BIT'
    def __init__(self,name,rollno):
        print('execute constructor')
        self.name=name
        self.rollno=rollno

    def info(self):
        #print(self)
        self.name_roll = self.name + self.rollno
        return self.name,self.rollno,self.name_roll

    @classmethod
    def clgname(cls):
        return  cls.cname


    @staticmethod
    def sepratemethod(x,y):
        return x+y




s1=Test('rahul','162IT172')

s2=Test('rnr','162IT162')
print(s1.info())
#print(s1.__dict__)