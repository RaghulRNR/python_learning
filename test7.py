#Nested function:
class A:
    def __init__(self,a,b):
        print("This is constructor")
        self.a=a
        self.b=b
    def general(self):
        sum(self.a,self.b)
        #product(self.a,self.b)
    def sum(a,b):
        print('a+b=',a+b)
    def product(a,b):
        print('a*b=',a*b)

t1=A(10,20)
t1.general()