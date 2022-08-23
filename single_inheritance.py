class Parent:
    def m1(self):
        print("parent class m1 ")
class Child(Parent):
    def m2(self):
        print("Child class M2")

#accessing parent class method with child class reference variable
c=Child()
c.m1()
c.m2()
