#Nested Inner class:
class Outer:
    def __init__(self):
        print('Inside outer class')
    class Inner:
        def __init__(self):
            print('Inside inner class')

        def display(self):
            print('inside display method')

#Outer().Inner().display()
o=Outer()
i=o.Inner()
i.display()
