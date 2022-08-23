class P:
    a=10
    def __init__(self):
        self.b=20

class C(P):
    def m1(self):
        print(super().a)
        #print(super().b)#this will not work because we can call by self.a itself


c=C()
c.m1()

print("*"*100)

#example-2:

class P:

    def __init__(self):
        print("Constructor Method")
    def m1(self):
        print("Instance Method")
    @classmethod
    def m2(cls):
        print("Class Method")
    @staticmethod
    def m3():
        print("Static  Method")

class C(P):
    def m1(self):#if we use class and static method ,it is throwing error while calling constructor
        super().__init__()
        super().m1()
        super().m2()
        super().m2()
        #print(super().b)#this will not work because we can call by self.a itself


c=C()
c.m1()