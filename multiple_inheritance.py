class Parent1:
    def m1(self):
        print("parent class m1 ")

class Parent2:
    def m1(self):
        print("Child class M2")

class child(Parent1,Parent2):
    def m3(self):
        print("Grand Child class M3")

#both parent has m1,it will execute parent 1 method because in child class parent1 has first priority
#if we interchange parent order then parent2 methos will execute
c=child()
c.m1()
c.m3()
