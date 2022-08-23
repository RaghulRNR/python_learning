#counting no of objects

class Test:

    count=0

    def __init__ (self):

        Test.count=Test.count+1

    @classmethod
    def noOfObjects(cls):
        print("No of object created is",Test.count)


t1=Test()
t2=Test()

Test.noOfObjects()