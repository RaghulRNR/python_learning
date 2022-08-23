class A:
    def m1(self):
         print('Class A method')
class B(A):
    def m1(self):
        print('Class B method')
class C(B):
    def m1(self):
        print('Class C method')
class D(C):
    def m1(self):
        #C.m1(self)#-1st way
        super(D,self).m1()#-2nd Way

d=D()
d.m1()

