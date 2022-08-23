class Test:
    def __init__(self,a=None,b=None,c=None):
        self.a=a
        self.b=b
        self.c=c
    def sum(self):
        if(self.a!=None and self.b!=None and self.c!=None):
            return  self.a+self.b+self.c
        elif(self.a!=None and self.b!=None):
            return  self.a+self.b
        else:
            print("pass more than one argument")


print(Test(10,20).sum())
