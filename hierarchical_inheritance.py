class Parent:
    def m1(self):
        print("Parent class method 1")
class Child1(Parent):
    def m2(self):
        print("Child 1 class method 2")
class Child2(Parent):
    def m3(self):
        print("Child 2 class method 3")

#Child 1 class obtain m1 and m2 method
c1=Child1()
c1.m1()
c1.m2()

#Child 2 class obtain m1 and m3 method
c2=Child2()
c2.m1()
c2.m3()