class Parent:
    def m1(self):
        print("parent class m1 ")

class Child(Parent):
    def m2(self):
        print("Child class M2")

class grandChild(Child):
    def m3(self):
        print("Grand Child class M3")

#accessing parent class method with child class reference variable-->
gc=grandChild()
gc.m1()
gc.m2()
gc.m3()